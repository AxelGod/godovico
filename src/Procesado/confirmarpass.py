import src.Conexion.consultar as db


def confir(user, passw):
    response = db.consultar('SELECT id_usuario FROM usuario WHERE nombre_usuario="'+user +
                 '" AND contraseña_usuario="'+passw+'"')
    if response:
        return response
    return (False)
