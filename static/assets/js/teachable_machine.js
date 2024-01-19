    // More API functions here:
    // https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image

    // the link to your model provided by Teachable Machine export panel
    const URL = "https://teachablemachine.withgoogle.com/models/EKNQW_21J/";

    let model, labelContainer, maxPredictions;
    let uploadedImage;

    function handleImageUpload(event) {
        const file = event.target.files[0];
        const reader = new FileReader();
        reader.onload = function (e) {
        const img = new Image();
        img.src = e.target.result;
        img.onload = async function () {
            uploadedImage = img;
            const imagePreview = document.querySelector(".image");
            imagePreview.style.backgroundImage = `url(${img.src})`;
            predict();
        };
        };
        reader.readAsDataURL(file);
    }
    // Load the image model
    async function init() {
        const modelURL = URL + "model.json";
        const metadataURL = URL + "metadata.json";

        // load the model and metadata
        model = await tmImage.load(modelURL, metadataURL);
        maxPredictions = model.getTotalClasses();

        labelContainer = document.getElementById("label-container");
        for (let i = 0; i < maxPredictions; i++) {
            labelContainer.appendChild(document.createElement("div"));
        }
    }

    // Predict on the uploaded image
    async function predict() {
        // predict can take in an image, video, or canvas HTML element
        const prediction = await model.predict(uploadedImage);
        let maxPrediction = 0;
        let maxPredictionIndex = 0;

        for (let i = 0; i < maxPredictions; i++) {
            const probability = prediction[i].probability.toFixed(2) * 100;
            if (probability > maxPrediction) {
                maxPrediction = probability;
                maxPredictionIndex = i;
            }
        }

        const maxPredictionLabel =
            "The result is : " +
            maxPrediction.toFixed(2) +
            "%  " +
            prediction[maxPredictionIndex].className +
            " Image";
            
        labelContainer.innerHTML = maxPredictionLabel;
    }