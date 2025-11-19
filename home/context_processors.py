

from django.core.cache import cache

def get_categories_n_subcats(request):
    # Tries to get the data from the cache to optimize performance by querying only once
    # instead of doing it every time
    categories_dropmenu = cache.get('categories_dropmenu')
    
    if not categories_dropmenu:
        
        categories_dropmenu = get_categories_n_subcategories(from_cache=False)
        # Save the data in the cache for 1 hour (3600 seconds)
        # cache.set('categories_dropmenu', categories_dropmenu, 3600)
    
    return {'categories_dropmenu': categories_dropmenu}


def get_categories_n_subcategories(
    from_cache=True, 
    from_dashboard=False,
    values_cat: tuple = ('id', 'name', 'slug'),
    values_sub: tuple = ('id', 'name', 'slug', 'degree_program_id')
):
    """
    Retrieves a dictionary mapping each non-default product category to its corresponding list of subcategories.

    Parameters:
        from_cache (bool, optional): If True, attempts to retrieve the result from cache. 
            Defaults to True.
        values_cat (tuple, optional): Fields of the category model to include in the output. 
            Defaults to ('id', 'name', 'slug').
        values_sub (tuple, optional): Fields of the subcategory model to include in the output. 
            Defaults to ('id', 'name', 'slug', 'category_id').

    Returns:
        dict: A dictionary where:
            - Each key is a category ID (int).
            - Each value is a dictionary with:
                - 'category': a dict representing the category (with selected fields).
                - 'subcategories': a list of subcategory dicts (or None if no subcategories).

    Example:
        {
            1: {
                'category': {'id': 1, 'name': 'Electronics', 'slug': 'electronics'},
                'subcategories': [
                    {'id': 10, 'name': 'Phones', 'slug': 'phones', 'category_id': 1},
                    {'id': 11, 'name': 'Laptops', 'slug': 'laptops', 'category_id': 1}
                ]
            },
            2: {
                'category': {'id': 2, 'name': 'Furniture', 'slug': 'furniture'},
                'subcategories': None
            }
        }
        
    Use Template:
        {% for item in categories_dropmenu.values %}
            {{ item.category.id }}
            {% if item.subcategories %}
                {% for subcat in item.subcategories %}
                    {{ item.category.name }} - {{ subcat.slug }}
    """
    if from_cache:
        categories_dropmenu = cache.get('categories_dropmenu')
        
        if categories_dropmenu and from_dashboard:
            categories_list = list(categories_dropmenu.values())
            return categories_list
        
        if categories_dropmenu:
            return categories_dropmenu
            
    # name__isnull=False 
    from posts.models import Subject, Degree
    subjects = Subject.objects.all().order_by('name').values(*values_sub) 
    degrees = Degree.objects.all().order_by('name').values(*values_cat)
    
    # Create a dictionary mapping each category to its subcategories (if any) 
    subcats_by_cat = {}
    for sub in subjects:
        cat_id = sub['degree_program_id']
        if cat_id not in subcats_by_cat:
            subcats_by_cat[cat_id] = []
        subcats_by_cat[cat_id].append(sub)

    # Construir el diccionario final
    categories_dropmenu = {}
    for cat in degrees:
        cat_id = cat['id']
        categories_dropmenu[cat_id] = {
            'category': cat,
            'subcategories': subcats_by_cat.get(cat_id) or []
        }
        
    if categories_dropmenu and from_dashboard:
        categories_list = list(categories_dropmenu.values())
        return categories_list

    return categories_dropmenu