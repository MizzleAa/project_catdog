import axios from "axios";

const baseURL = "http://127.0.0.1:8000/catdog/";

const api = axios.create({
    baseURL: baseURL,
});

export default api;
