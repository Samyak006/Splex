import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:3000",
  headers: {
    "Content-Type": "application/json",
  },
});

api.interceptors.request.use(
    (response)=>response,
    (error)=>{
        console.error("API Request Error:", error);
        return Promise.reject(error);
    }
)
export default api;