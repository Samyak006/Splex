// import type { IRegister } from "@/types/register";

export const Register = ()=>{
    return (
        <div className="Register">
            <h2>Register</h2>
            <input type="text" placeholder="Username" />
            <input type="password" placeholder="Password" />
            <input type="email" placeholder="Email" />
            <input type="text" placeholder="Name" />
        </div>
    );
}