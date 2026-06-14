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
    
    drawEdges([
    {
        source: "Repository",
        target: "Backend"
    },
    {
        source: "Backend",
        target: "Frontend"
    },
    {
        source: "Backend",
        target: "AI"
    },
    {
        source: "Backend",
        target: "Database"
    }
    ]);
}


function renderLayers(layers) {
        
    if (!layers.Database) {

            layers.Database = {

                count: 0,

                files: [],

                avg_confidence: 0

            };

        }

    layerContainer.innerHTML = "";

    const positions = {

        Backend: {
            left: "40%",
            top: "220px"
        },

        Frontend: {
            left: "10%",
            top: "430px"
        },

        AI: {
            left: "70%",
            top: "430px"
        },

        Database: {
            left: "40%",
            top: "640px"
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
            card.id = `node-${layerName}`;

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

            layerContainer.appendChild(card);

        }

    );

}


function showDetails(layerName, info){

    let html = `

    <h2>${layerName}</h2>

    <p><b>Total Files:</b> ${info.count}</p>

    <p><b>Average Confidence:</b> ${info.avg_confidence ?? 0}</p>

    <hr>

    `;

    info.files.forEach(file=>{

        html += `

    <div
        style="
            margin-top:10px;
            padding:10px;
            border-radius:10px;
            background:#f3f4f6;
            border-left:4px solid #2563eb;
        "
    >

        📄 ${file.path}

    </div>

    `;
    });

    detailsContent.innerHTML = html;

}

function drawEdges(edges) {

    const svg = document.getElementById(
        "connection-svg"
    );
    document.getElementById(
        "repository-node"
    ).id = "node-Repository";

    // Clear previous drawing
    svg.innerHTML = "";

    // Create arrow marker
    const defs = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "defs"
    );

    const marker = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "marker"
    );

    marker.setAttribute("id", "arrowhead");
    marker.setAttribute("viewBox", "0 0 10 10");
    marker.setAttribute("refX", "8");
    marker.setAttribute("refY", "5");
    marker.setAttribute("markerWidth", "8");
    marker.setAttribute("markerHeight", "8");
    marker.setAttribute("orient", "auto");

    const arrow = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "path"
    );

    arrow.setAttribute(
        "d",
        "M 0 0 L 10 5 L 0 10 Z"
    );

    arrow.setAttribute(
        "fill",
        "#2563eb"
    );

    marker.appendChild(arrow);
    defs.appendChild(marker);
    svg.appendChild(defs);

    const graph =
        document.getElementById(
            "graph-area"
        );

    const graphRect =
        graph.getBoundingClientRect();

    edges.forEach(edge => {

        const source =
            document.getElementById(
                `node-${edge.source}`
            );

        const target =
            document.getElementById(
                `node-${edge.target}`
            );

        if (!source || !target) {
            return;
        }

        const s =
            source.getBoundingClientRect();

        const t =
            target.getBoundingClientRect();

        const x1 =
            s.left +
            s.width / 2 -
            graphRect.left;

        const y1 =
            s.top +
            s.height / 2 -
            graphRect.top;

        const x2 =
            t.left +
            t.width / 2 -
            graphRect.left;

        const y2 =
            t.top +
            t.height / 2 -
            graphRect.top;

        const controlY =
            (y1 + y2) / 2;

        const path =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "path"
            );

        path.setAttribute(
            "d",
            `
            M ${x1} ${y1}
            C ${x1} ${controlY},
              ${x2} ${controlY},
              ${x2} ${y2}
            `
        );

        path.setAttribute(
            "fill",
            "none"
        );

        path.setAttribute(
            "stroke",
            "#2563eb"
        );

        path.setAttribute(
            "stroke-width",
            "4"
        );

        path.setAttribute(
            "marker-end",
            "url(#arrowhead)"
        );

        svg.appendChild(path);

    });
    path.classList.add("connection");

}

loadArchitecture();