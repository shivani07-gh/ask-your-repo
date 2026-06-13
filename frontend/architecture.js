const layerContainer =
    document.getElementById("layer-container");

const detailsContent =
    document.getElementById("details-content");


async function loadArchitecture() {

    const response = await fetch(
        "http://127.0.0.1:8000/visualize"
    );

    const data = await response.json();

    console.log(data);

    window.architectureData = data;
    renderLayers(data.layers); 
}


function renderLayers(layers) {

    layerContainer.innerHTML = "";

    const positions = {

    Frontend: {
        left: "8%",
        top: "300px"
    },

    Backend: {
        left: "40%",
        top: "300px"
    },

    AI: {
        left: "72%",
        top: "300px"
    },

    Database: {
        left: "40%",
        top: "520px"
    }

};
    Object.entries(layers).forEach(

        ([layerName, info]) => {

            const card =
                document.createElement("div");

            card.className =
                "layer-card";

            const emoji = {
                Frontend: "🖥️",
                Backend: "⚙️",
                AI: "🧠",
                Database: "🗄️"
            };

            card.innerHTML = `

                <div style="font-size:36px">
                    ${emoji[layerName] || "📦"}
                </div>

                <h2>${layerName}</h2>

                <p>${info.count} Files</p>

            `;

            const pos =
                positions[layerName];

            if (pos) {

                card.style.left =
                    pos.left;

                card.style.top =
                    pos.top;
            }

            card.onclick = () => {

                document
                    .querySelectorAll(".layer-card")
                    .forEach(x => {

                        x.style.border =
                            "none";

                    });

                card.style.border =
                    "3px solid #2563eb";

                showDetails(
                    layerName,
                    info
                );

            };

            layerContainer
                .appendChild(card);

        }

    );

}


function showDetails(layerName, info){

    let html = `

        <h2>${layerName}</h2>

        <p>
            <b>Files:</b>
            ${info.count}
        </p>

        <hr>

    `;

    info.files.forEach(file=>{

        html += `

            <div
                style="
                    padding:10px;
                    margin-top:8px;
                    border-radius:8px;
                    background:#f3f4f6;
                "
            >

                📄 ${file.path}

            </div>

        `;

    });

    detailsContent.innerHTML = html;

}


loadArchitecture();