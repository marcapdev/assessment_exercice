# Instrucciones para lanzamiento en local

El proyecto está preparado para lanzarse con docker.

- Docker
    - Abrir terminal en la carpeta raiz del proyecto
    - Lanzar el comando: ***SETTINGS="backend_assessment_exercise.conf.local" docker compose up*** para entorno local y
      ***SETTINGS="backend_assessment_exercise.conf.production" docker compose up*** para testear entorno producción de
      forma local
    - entrar en el contenedor de docker con nombre "web" y lanzar las migraciones de django (python manage.py migrate
      --settings=backend_assessment_exercise.conf.local)
    - He abierto el puerto 5555 para alojar el app flower para consultar el estado de las tareas asincronas
    - Opcional lanzar test:
        - python manage.py test --settings=backend_assessment_exercise.conf.local
          ![Flower](https://user-images.githubusercontent.com/116147283/197024297-bbbeb723-275c-4c93-b21b-81af4f5bad7a.png)

Si se lanza sin docker anoto las versiones de python que he usado: Python 3.10.8, pip 22.2.2.

# EndPoints

- URLs propuestas para cada endpoint:
    - Registro: ^/api/VERSION_API/signup/$
    - Perfil: ^/api/VERSION_API/profile/$
    - Obtener Token Acceso: ^/api/VERSION_API/api-token-auth/$

# ¿Cuántas consultas hace cada endpoint a la BD?

- Registro:
    - se hacen 2 llamadas.
        - La primera consulta se realiza en el paso de la validación del serializador para comprobar que no existe una
          entrada en la BD con ese email (No venía en el enunciado, pero he optado que el campo email fuera unique, si
          fuera
          necesario se puede desactivar la validación del campo en el serializador)
        - La segunda consulta es la sentencia insert
        - Ejemplo log BD

> statement: SELECT (1) AS "a" FROM "api_user" WHERE "api_user"."email" = 'marc.amposta.perez93@gmail.com' LIMIT 1
>
> statement: BEGIN
>
> statement: INSERT INTO "api_user" ("first_name", "last_name", "email", "phone", "hobbies", "validated_phone", "
> validated_email") VALUES ('Marc', 'Amposta Pérez', 'marc.amposta.perez93@gmail.com', '+34616650957', 'test', false,
> false) RETURNING "api_user"."id"
>
> statement: COMMIT

- Perfil:
    - se hace 1 llamada
        - La llamada es la sentencia select
        - Ejemplo log DB

> statement: SELECT "api_user"."id", "api_user"."first_name", "api_user"."last_name", "api_user"."email", "api_user"."
> phone", "api_user"."hobbies", "api_user"."validated_phone", "api_user"."validated_email" FROM "api_user" WHERE "
> api_user"."id" = 1 LIMIT 21

- Obtener Token
    - Se hace 1 llamada
        - La llamada es la sentencia select
        - Ejemplo log DB

> statement: SELECT "authtoken_token"."key", "authtoken_token"."user_id", "authtoken_token"."created", "api_user"."id"
> , "api_user"."password", "api_user"."last_login", "api_user"."is_superuser", "api_user"."first_name", "api_user"."
> last_name", "api_user"."is_staff", "api_user"."is_active", "api_user"."date_joined", "api_user"."phone", "api_user"."
> email", "api_user"."hobbies", "api_user"."validated_phone", "api_user"."validated_email" FROM "authtoken_token" INNER
> JOIN "api_user" ON ("authtoken_token"."user_id" = "api_user"."id") WHERE "authtoken_token"."key" = '
> fc07442366bd80fea29100e9673684a3f5c15400' LIMIT 21

# ¿Puedes poner un ejemplo de petición (tipo curl) por cada endpoint?

- Adjunto también en el directorio raiz del repositorio un json con la colección de postman que he usado
  (BackendAssessment.postman_collection.json)
- Registro:
    - curl --location --request POST 'http://localhost:8000/api/1.0.0/signup/' --form 'first_name="Marc"' --form '
      last_name="Amposta Pérez"' --form 'email="marc.amposta.perez93@gmail.com"' --form 'phone="+34 616650957"' --form '
      hobbies="test"'
- Perfil:
    - curl --location --request GET 'http://localhost:8000/api/1.0.0/profile/1'

# ¿Qué te ha parecido la prueba? ¿Te ha gustado? ¿Te ha parecido sencilla, media, compleja?

- Es una prueba bastante completa, sin duda ayuda a ver como se desenvuelve el desarrollador. Incluye la toma
  decisiones de como abordar ciertos escenarios (como configurar entornos en local/prod y comportamientos distintos
  según el entorno) así como el
  desarrollo de tareas más simples, pero que siempre están presentes como generación de modelos, registro en BD,
  consultas en BD y uso de transacciones. La complejidad no ha sido excesiva aunque dicho esto casi siempre es posible
  encontrar formas de mejorar como se ha abordado la solución, tras revisiones de código o tal y como el proyecto va
  escalando.

# ¿Hay algún punto que te haya parecido confuso de la prueba?

- En el apartado de registrar y mostrar el estado de la validación del SMS y MAIL entiendo que estos campos siempre van
  a aparecer como no validados, ya que el alcance de la tarea no incluye el envío de los mensajes asi como la
  posterior validación por el usuario si no he entendido mal, tal vez habría destacado esto en el enunciado.
- No tenía muy claro si aunque el password no aparece como uno de los inputs en la description de registro de usuario,
  lo podemos añadir.

# ¿Has aprendido algo con esta prueba?

- No había investigado mucho sobre el envio de sms desde python/django así que he podido ver un poco que librerías
  existen relacionadas con el tema.

# ¿Cuánto tiempo has tardado en hacer la prueba?

- Entre plantear las soluciones, desarollar y revisar código unas 8-10 h

# ¿Qué es lo más divertido que has desarrollado? ¿Qué es lo que más te gusta desarrollar?

- En el proyecto de fin de carrera tuve la oportunidad de trabajar con websockets para obtener el stream de audio del
  micro y transcribirlo mediante un api de terceros. me siento comodo desarrollando apps web que den pie a tener
  variedad. Pero me suele gustar todo lo relacionado con la informática.

# ¿Qué es lo que más odias desarrollar?

- Tal vez no llego a odiar, pero cuando son tareas más monotonas durante un tiempo prolongado. Como pueden ser tal vez
  generar algunos excels o cosas por el estilo.

# ¿Tienes manías desarrollando? ¿Cuáles son?

- Diría que no. Un estilo de programar sí pero manía como tal creo que no.

# Después de hacer la prueba, ¿tienes algunas dudas extras sobre cómo trabajamos?

- Me gustaria ver como se origanizan las tareas que tipos de herramientas se usan, como es la estructura del proyeto,
  casos de usos y implementaciones más concretas

# ¿Cambiarías algo de la prueba para completarla con algo que consideres importante?

