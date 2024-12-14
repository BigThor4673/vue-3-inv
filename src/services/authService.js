import { db, auth, googleProvider } from "../firebase";

async function loginWithGoogle() {
  try {
    const result = await auth.signInWithPopup(googleProvider);
    const user = result.user;
    console.log("Usuario autenticado:", user.email);
    return user;
  } catch (error) {
    console.error("Error en la autenticación con Google:", error);
    throw error;
  }
}

async function checkUserAccess(email) {
    try {
      const userDocRef = db.collection("allowedUsers").doc(email);
      const userDoc = await userDocRef.get();
  
      if (userDoc.exists) {
        console.log("Usuario permitido:", email);
        return true; // Usuario tiene acceso permitido
      } else {
        console.warn("Usuario no permitido:", email);
        return false; // Usuario no tiene acceso permitido
      }
    } catch (error) {
      console.error("Error verificando acceso del usuario:", error);
      return false;
    }
  }

export { loginWithGoogle, checkUserAccess };
