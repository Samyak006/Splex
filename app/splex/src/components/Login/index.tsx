import type { ILogin } from "@/types/login";

export const Login = ({login}:{login:ILogin}) =>{
    return (
        <div className="Login">
            <h2>Login</h2>
            <p>Username: {login.username}</p>
            <p>Password: {login.password}</p>
        </div>
    );
}