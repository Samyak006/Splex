
export const Register = () => {
    const {handleRegister} = useRegister();
    return (
        <div className="Register">
            <h2>Register</h2>
            <form onSubmit={handleRegister}>
                <input type="text" placeholder="Username" />
                <input type="password" placeholder="Password" />
                <input type="email" placeholder="Email" />
                <input type="text" placeholder="Name" />
            </form>
        </div>
    );
}