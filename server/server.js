const express = require('express');
const { exec } = require('child_process');
const path = require('path');
const fs = require('fs');
const cors = require('cors');
const multer = require('multer');

const app = express();
const PORT = 3000;

// Middleware pour interpréter les données JSON dans le corps des requêtes
app.use(express.json());

// Configuration de CORS
const corsOptions = {
  origin: ['http://localhost:4200', 'http://localhost:3000'],
  methods: ['GET', 'POST', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
};
app.use(cors(corsOptions));
app.options('*', cors());

// Middleware pour le téléchargement de fichiers
const upload = multer({ dest: 'uploads/' });

// Route pour générer un CSV à partir de données JSON
app.post('/generate-csv', (req, res) => {
  const data = req.body;

  // Vérifier que les données sont bien un tableau d'objets
  if (!Array.isArray(data) || data.length === 0) {
    return res.status(400).send("Le corps de la requête doit contenir un tableau d'objets.");
  }

  // Sauvegarder les données JSON dans un fichier temporaire
  const inputFilePath = path.join(__dirname, 'input_data.json');
  fs.writeFileSync(inputFilePath, JSON.stringify(data));

  // Exécuter le script Python en passant le fichier JSON en argument
  exec(`python generate_csv.py ${inputFilePath}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Erreur lors de l'exécution du script Python: ${error.message}`);
      return res.status(500).send("Erreur lors de la génération du CSV");
    }
    if (stderr) {
      console.error(`Erreur dans le script Python: ${stderr}`);
    }
    console.log(`Sortie du script Python: ${stdout}`);

    // Chemin vers le fichier CSV généré
    const filePath = path.join(__dirname, 'output.csv');

    // Envoyer le fichier CSV en téléchargement
    res.download(filePath, 'output.csv', (err) => {
      if (err) {
        console.error(`Erreur lors de l'envoi du fichier CSV: ${err.message}`);
        res.status(500).send("Erreur lors de l'envoi du fichier CSV");
      }

      // Supprimer le fichier JSON temporaire après l'envoi du CSV
      fs.unlinkSync(inputFilePath);
    });
  });
});

// Route pour supprimer un fichier CSV
app.delete('/delete-csv', (req, res) => {
  const filePath = path.join(__dirname, 'output.csv');

  // Vérifier si le fichier existe
  fs.access(filePath, fs.constants.F_OK, (err) => {
    if (err) {
      return res.status(404).send("Le fichier output.csv n'existe pas.");
    }

    // Supprimer le fichier
    fs.unlink(filePath, (err) => {
      if (err) {
        console.error(`Erreur lors de la suppression du fichier: ${err.message}`);
        return res.status(500).send("Erreur lors de la suppression du fichier.");
      }

      res.send("Le fichier output.csv a été supprimé avec succès.");
    });
  });
});

// Route pour télécharger une vidéo
app.post('/upload-video', upload.single('video'), (req, res) => {
  const file = req.file;

  if (!file) {
    return res.status(400).send("Aucun fichier vidéo n'a été envoyé.");
  }

  console.log(`Fichier reçu : ${file.originalname}`);

  // Simuler la génération d'un fichier CSV
  const outputCsvPath = path.join(__dirname, 'output.csv');
  fs.writeFileSync(outputCsvPath, 'id,name\n1,Test');

  res.download(outputCsvPath, 'output.csv', (err) => {
    if (err) {
      console.error("Erreur lors de l'envoi du fichier CSV:", err.message);
      res.status(500).send("Erreur lors de l'envoi du fichier CSV.");
    }

    // Supprimez le fichier temporaire vidéo après traitement
    fs.unlinkSync(file.path);
  });
});

// Route pour traiter une vidéo et obtenir des informations (exemple)
app.post('/get-video', async (req, res) => {
  try {
    // Exemple de traitement d'une vidéo
    const framesDir = 'frames';
    await createFrame();
    const allFiles = fs.readdirSync(framesDir);
    const fullPath = path.join(framesDir, allFiles[0]);

    // Appeler une fonction Python pour traiter une image spécifique
    const plaque = 'DA-861-LY';
    const json = await getFunction(fullPath, plaque);

    res.json({ ok: json });
  } catch (err) {
    console.error(err.message);
    res.status(500).send("Erreur lors du traitement de la vidéo.");
  }
});

// Lancer le serveur
app.listen(PORT, () => {
  console.log(`Serveur lancé sur http://localhost:${PORT}`);
});

// Fonctions auxiliaires
async function getFunction(fullPath, plaque) {
  return new Promise((resolve, reject) => {
    exec(`python getFunction.py "${fullPath}" "${plaque}"`, (error, stdout, stderr) => {
      if (error || stderr) {
        return reject(error || stderr);
      }
      resolve(stdout.trim());
    });
  });
}

async function createFrame() {
  return new Promise((resolve, reject) => {
    exec('python get-frames.py', (error, stdout, stderr) => {
      if (error || stderr) {
        return reject(error || stderr);
      }
      resolve();
    });
  });
}
