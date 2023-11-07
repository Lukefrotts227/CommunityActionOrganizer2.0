function addressAutocomplete(containerElement, callback, options){
    const MIN_ADDRESS_LENGTH = 3;
    const DEBOUNCE_DELAY = 300;

    inputElement.addEventListener("input", function(e) {
        if(currentTimeout){
            clearTimeout(currentTimeout); 
        }

        if (currentPromiseReject) {
            currentPromiseReject({
              canceled: true
            });
        }

        if (!currentValue || currentValue.length < MIN_ADDRESS_LENGTH) {
            return false;
        }
        
    })
}