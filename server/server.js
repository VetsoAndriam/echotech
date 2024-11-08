const express = require("express");
const { exec } = require("child_process");
const path = require("path");
const fs = require("fs");
const { log } = require("console");
const { stdout } = require("process");
const app = express();
const PORT = 3000;

// Middleware pour interpréter les données JSON dans le corps des requêtes
app.use(express.json());

// Route pour post la video
app.post("/get-video", async (req, res) => {
  //Inserer le script qui permet de recupérer une vidéo en image
        // await createFrame()
            const allFiles = fs.readdirSync("frames");
            const file = allFiles[1];
            const fullPath = path.join("frames", file);
            console.log("fullPath", fullPath);

  //INSERER METHODE GET PLAQUE
  const getPlaque = "DA-861-LY";
  ///METHODE getFunction
  const json = await getFunction(fullPath,getPlaque)
  console.log(json);
  return res.json({ ok: json });
});

//   allFiles.forEach(file => {
//     const fullPath = path.join("frames", file)
//     const allData = exec(`python get-function.py ${fullPath} ${getPlaque}`)
//     console.log(allData);
//   })

// exec(`python get-function.py ${fullPath} ${getPlaque}`, (stdout) => {
// console.log(stdout);

// })

app.post("/generate-csv", (req, res) => {
  // Récupérer les données JSON envoyées dans le corps de la requête
  const data = req.body;

  // Vérifier que les données sont bien un tableau d'objets
  if (!Array.isArray(data) || data.length === 0) {
    return res
      .status(400)
      .send("Le corps de la requête doit contenir un tableau d'objets.");
  }

  // Sauvegarder les données JSON dans un fichier temporaire
  const inputFilePath = path.join(__dirname, "input_data.json");
  fs.writeFileSync(inputFilePath, JSON.stringify(data));

  // Exécuter le script Python en passant le fichier JSON en argument
  exec(`python generate_csv.py ${inputFilePath}`, (error, stdout, stderr) => {
    if (error) {
      console.error(
        `Erreur lors de l'exécution du script Python: ${error.message}`
      );
      return res.status(500).send("Erreur lors de la génération du CSV");
    }
    if (stderr) {
      console.error(`Erreur dans le script Python: ${stderr}`);
    }
    console.log(`Sortie du script Python: ${stdout}`);

    // Chemin vers le fichier CSV généré
    const filePath = path.join(__dirname, "output.csv");

    // Envoyer le fichier CSV en téléchargement
    res.download(filePath, "output.csv", (err) => {
      if (err) {
        console.error(`Erreur lors de l'envoi du fichier CSV: ${err.message}`);
        res.status(500).send("Erreur lors de l'envoi du fichier CSV");
      }

      // Supprimer le fichier JSON temporaire après l'envoi du CSV
      fs.unlinkSync(inputFilePath);
    });
  });
});

// Route pour supprimer le fichier CSV
app.delete("/delete-csv", (req, res) => {
  const filePath = path.join(__dirname, "output.csv");

  // Vérifier si le fichier existe
  fs.access(filePath, fs.constants.F_OK, (err) => {
    if (err) {
      // Si le fichier n'existe pas
      return res.status(404).send("Le fichier output.csv n'existe pas.");
    }

    // Supprimer le fichier
    fs.unlink(filePath, (err) => {
      if (err) {
        console.error(
          `Erreur lors de la suppression du fichier: ${err.message}`
        );
        return res
          .status(500)
          .send("Erreur lors de la suppression du fichier.");
      }

      // Confirmation de la suppression
      res.send("Le fichier output.csv a été supprimé avec succès.");
    });
  });
});

// Lancer le serveur
app.listen(PORT, () => {
  console.log(`Serveur lancé sur http://localhost:${PORT}`);
});

async function getFunction(fullPath, plaque) {
    return new Promise((resolve, reject) =>{
        exec(`python getFunction.py "${fullPath}" "${plaque}"`, (stdout, stderr) => {
          console.log(stdout);

          // resolve(stdout);
    })
  });
}

async function createFrame() {
    return new Promise((resolve, reject) =>{
        exec(`python get-frames.py`, (error, stdout, stderr) => {
          if (stdout) {
            console.log(`Sortie du script Python: ${stdout}`);
            resolve(fs.readdirSync("frames"));
        }else{
            reject(new Error(stderr || "Erreur lors de l'exécution du script"));
        }
    });
  });
}
