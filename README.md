# Student Score Predictor

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python Version"/>
  <img src="https://img.shields.io/badge/FastAPI-0.116.1-orange" alt="FastAPI Version"/>
  <img src="https://img.shields.io/badge/Pydantic-2.11.7-green" alt="Pydantic Version"/>
  <img src="https://img.shields.io/badge/Uvicorn-0.35.0-red" alt="Uvicorn Version"/>
</p>

A minimal web application that predicts student exam scores based on the number of study hours using a simple Linear Regression model.

---

## 🚀 Demo

- 🔗 **Frontend (GitHub Pages):** [Live Demo](https://anjalbhattarai79.github.io/student-score-prediction/)
- 🔗 **API Backend (Render):** [FastAPI on Render](https://student-score-prediction-br3c.onrender.com/)

---

## 📦 Project Structure

```text
student-score-prediction/
├── Model_Training_Phase/
│   ├── data.csv              # Dataset used for training
│   └── notebook.ipynb        # Jupyter notebook for model training
├── app/
│   ├── main.py               # FastAPI app with ML logic
│   ├── model.pkl             # Trained linear regression model
│   ├── requirements.txt      # Project dependencies
├── .gitignore
├── Dockerfile                # Docker config to run app
├── index.html                # Frontend UI page (single input + output)
├── start.sh                  # Startup script for Render
```

---

## 🧠 How It Works

1. **User Input:** Enter study hours on the frontend.
2. **API Request:** Frontend sends the data as JSON to the FastAPI backend.
3. **Prediction:** Backend loads a pre-trained linear regression model and returns the predicted score.
4. **Result:** Frontend displays the prediction in real time.

---

## 🐋 Deployment

### 📌 Docker

***View on [Docker Hub](https://hub.docker.com/repository/docker/anjalbhattarai79/student-score-predictor/general)***
<br><br>
To run locally using Docker:

```bash
docker pull anjalbhattarai79/student-score-predictor:latest
docker run -p 8000:8000 anjalbhattarai79/student-score-predictor:latest
```

Or build from source:

```bash
docker build -t student-score-predictor .
docker run -p 8000:8000 student-score-predictor
```



---

### 📌 Render

- Deployed backend: [student-score-prediction-br3c.onrender.com](https://student-score-prediction-br3c.onrender.com)
- Docker-based deployment using [Render](https://render.com/)
- `start.sh` is used as the entrypoint for launching the Uvicorn server


<br>

## 📥 API Usage

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Content-Type:** `application/json`

**Example Request:**

```json
{
  "hours": 5.5
}
```

**Example Response:**

```json
{
  "predicted_score": 55.1
}
```


<br>

## 🤝 Contribution
Contributions, feedback, and suggestions are welcome! Feel free to open issues or pull requests.


