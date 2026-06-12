

export const useRegister = ():void => {
  const handleRegister = async (e: React.FormEvent<HTMLFormElement>) =>{
    e.preventDefault();
    api.post('/register').then((response) => {
        console.log("Registration successful:", response.data);
    }).catch((error) => {   
        console.error("Registration failed:", error);
    });
    return ()
    
  );
}
