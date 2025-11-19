







/**
 * Updates the price filter UI and product list based on the selected price range.
 * 
 * @param {HTMLElement} contProducts - The container element where product cards are rendered.
 */
function updateContPrices(sidebarCont) {
    
    const minRange = sidebarCont.querySelector('#min-range');
    const maxRange = sidebarCont.querySelector('#max-range');
    const spanMin = sidebarCont.querySelector('#min-val');
    const spanMax = sidebarCont.querySelector('#max-val');
    const track = sidebarCont.querySelector('.slider-track');

    if (!minRange || !maxRange) return;

    // Limpiar event listeners anteriores si existen
    if (minRange._updateSliderHandler) {
        minRange.removeEventListener('input', minRange._updateSliderHandler);
        maxRange.removeEventListener('input', minRange._updateSliderHandler);
    }

    // Get current min and max prices from product store (considering discounts)
    // const { min: minPrice, max: maxPrice } = ProductStore.getPriceRange();
    const minPrice = 5000.0;
    const maxPrice = 10000.0;

    console.log(`Precio mayor: ${minPrice} - Precio menor: ${maxPrice}`)

    // Set the actual limits for the range sliders
    minRange.min = minPrice;
    minRange.max = maxPrice;
    minRange.value = minPrice;

    maxRange.min = minPrice;
    maxRange.max = maxPrice;
    maxRange.value = maxPrice;

    // Set step size for slider increments (fixed to 100 in this example)
    const step = 100;
    minRange.step = step;
    maxRange.step = step;

    // Create a debounced function to filter products and update the UI
    const debouncedFilter = debounce((min, max) => {
        console.log('xd')

        // hacer movimiento visual al nuevo grupo de tarjetas
        // scrollToSection(contProducts, 'highlight-main');
    }, 800);

    const visualTrack = (min, max) => {
        // Update the visible min and max values text
        spanMin.textContent = min;
        spanMax.textContent = max;

        // Calculate slider percentages for the gradient background
        const range = maxPrice - minPrice;

        // evitar division por cero
        let percentMin = 0;
        let percentMax = 100;
        if (range > 0) {
            percentMin = ((min - minPrice) / range) * 100;
            percentMax = ((max - minPrice) / range) * 100;
        }

        // Set slider track background
        track.style.background = `linear-gradient(to right, 
            var(--bg-primary) ${percentMin}%,
            var(--main-color) ${percentMin}%,
            var(--main-color) ${percentMax}%,
            var(--bg-primary) ${percentMax}%)`;
    }



    // Function to handle slider input changes
    const updateSlider = (e = null) => {
        let min = parseInt(minRange.value);
        let max = parseInt(maxRange.value);

        // Prevent sliders from crossing over
        if (min > max) {
            if (e && e.target === minRange) {
                min = max;
                minRange.value = max;
            } else if (e) {
                max = min;
                maxRange.value = min;
            }
        }
        visualTrack(min, max);
        
        if (e) debouncedFilter(min, max);

        const spanPrice = sidebarCont.querySelector('.price-form');
        if (spanPrice) {
            spanPrice.textContent = formatNumberWithPoints(max);
            spanMin.value = 5000;
            spanMax.value = 10000;
        } 
    };

    // Guardar referencia a la función para poder eliminarla después
    minRange._updateSliderHandler = updateSlider;

    // Add event listeners
    minRange.addEventListener('input', updateSlider);
    maxRange.addEventListener('input', updateSlider);

    // Actualizar visualización inicial
    visualTrack(minPrice, maxPrice);
}





document.addEventListener('DOMContentLoaded', () => {

    const sidebarContsss = document.querySelectorAll('.form-search-tutor');
    if (sidebarContsss) {
        
        sidebarContsss.forEach(cont => updateContPrices(cont))
        // new TomSelect("#select-degrees");
    }

    const formSearch = document.getElementById("form-search-tutores");
    if (formSearch) {
        formSearch.addEventListener('submit', (e) => {
            // Obtener el valor de carrera
            const degreeSelect = formSearch.querySelector('[name="degree"]');
            const selectedDegree = degreeSelect.value;
            // Validar que se seleccionó una carrera (no el valor 0)
            if (selectedDegree === "0") {
                openAlert("Debe seleccionar una carrera antes de filtrar", "orange", 3000);
                e.preventDefault(); // Evita el envío del formulario
                return;
            }

            const subjectSelect = formSearch.querySelector('[name="subject"]');
            const selectedSubject = subjectSelect.value;
            // Validar que se seleccionó una carrera (no el valor 0)
            if (selectedSubject === "0") {
                openAlert("Debe seleccionar una materia antes de filtrar", "orange", 3000);
                e.preventDefault(); // Evita el envío del formulario
                return;
            }

            const modalidadSelect = formSearch.querySelector('[name="modalidad"]');
            const selectedModalidad = modalidadSelect.value;
            // Validar que se seleccionó una carrera (no el valor 0)
            if (selectedModalidad === "0") {
                openAlert("Debe seleccionar una Modalidad antes de filtrar", "orange", 3000);
                e.preventDefault(); // Evita el envío del formulario
                return;
            }
            
            // Si quieres validar más campos, puedes agregar aquí
            // Por ejemplo, validar que el precio mínimo no sea mayor al máximo
            const precioMin = parseInt(document.getElementById('min-val').textContent);
            const precioMax = parseInt(document.getElementById('max-val').textContent);
            
            if (precioMin > precioMax) {
                openAlert("El precio mínimo no puede ser mayor al precio máximo", "orange", 3000);
                e.preventDefault();
                return;
            }
            
            // Si pasa todas las validaciones, el formulario se envía normalmente
            // No hacemos preventDefault(), así que el submit tradicional funciona
        });
    }




    const formSolicitud = document.getElementById("form-solicitud");

    if (formSolicitud) {
        formSolicitud.addEventListener('submit', (e) => {

            e.preventDefault();

            // Obtener el valor del textarea
            const textTarea = formSolicitud.querySelector('#tarea');
            const inputTarea = textTarea.value.trim(); // .value en lugar de .input()

            // Validar que no esté vacío
            if (inputTarea === '') {
                openAlert("Debe completar la solicitud con sus temas de consulta.", "orange", 3000);
                textTarea.focus(); // Opcional: enfocar el campo
                return; // Detener la ejecución
            }

            openAlert("Registro una nueva solicitud con éxito", 'green', 3000)
        })
    }
    

    let globalPond = null;
    const form = document.getElementById('process-img')

    if (form) {
        form.addEventListener('submit', (e) => {
            openAlert("Debe seleccionar una materia", "orange", 3000)
            e.preventDefault();
        })
    

        function initInputImage(form) {
            const imageInput = form.querySelector('.image-input');
            const previewContainer = form.querySelector('.cont-img-previews');

            // 1. Limpieza inicial
            if (globalPond) {
                FilePond.destroy(globalPond);
                globalPond = null;
            }
            imageInput.value = '';
            previewContainer.innerHTML = '';

            // 2. Configurar FilePond con Compressor.js
            globalPond = FilePond.create(imageInput, {
                allowMultiple: true,
                acceptedFileTypes: ['image/*'],
                maxFiles: 5,
                // Deshabilita la cámara para priorizar la galería
                allowCamera: true,
                labelIdle: 'Arrastra tus imágenes o <span class="filepond--label-action"><b>Selecciona</b></span>',

                onaddfilestart: (file) => {
                    const originalFile = file.file;

                    new Compressor(originalFile, {
                        quality: 0.7,
                        maxWidth: 1024,
                        maxHeight: 1024,
                        success(result) {
                            const compressed = new File([result], originalFile.name, {
                                type: file.file.type, // esto es crucial
                                // type: 'image/jpeg',
                                lastModified: Date.now()
                            });

                            // Actualizamos preview manualmente si querés
                            updatePreview(compressed, previewContainer);
                        },
                        error(err) {
                            console.error("Compresión falló:", err);
                        }
                    });
                },
                onremovefile: () => {
                    previewContainer.innerHTML = '';
                }
            });

            
            // 3. Función de previsualización optimizada
            function updatePreview(file, container) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const img = document.createElement('img');
                    img.src = e.target.result;
                    img.classList.add('h-190');
                    container.appendChild(img);
                };
                reader.readAsDataURL(file);
            }
        }

        initInputImage(form);
    }
});