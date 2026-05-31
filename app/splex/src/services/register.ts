import type { IRegister } from "../types/register";
import api from "./api";

export const registerUser = async (userData:IRegister): Promise<IRegister> => {
    const response = await api.post('/register', userData);
    return response.data;
}