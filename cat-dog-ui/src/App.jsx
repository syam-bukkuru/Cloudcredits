import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
    setResult(null);
    if (selectedFile) {
      setImagePreview(URL.createObjectURL(selectedFile));
    }
  };

  const handleSubmit = async () => {
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/predict`, formData);
      setResult(res.data);
    } catch (error) {
      console.error("Prediction error:", error);
      alert("Prediction failed: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app" style={{ textAlign: "center", padding: "2rem" }}>
      <h1>🐶🐱 Cat or Dog Classifier</h1>

      <input type="file" onChange={handleFileChange} />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Predicting..." : "Predict"}
      </button>

      {imagePreview && (
        <div style={{ marginTop: "2rem" }}>
          <img
            src={imagePreview}
            alt="Uploaded"
            style={{ maxWidth: "300px", borderRadius: "12px" }}
          />
        </div>
      )}

      {result && (
        <div style={{ marginTop: "1.5rem" }}>
          <h2>Prediction: <span style={{ color: "#007bff" }}>{result.label.toUpperCase()}</span></h2>
          <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
        </div>
      )}
    </div>
  );
}

export default App;
