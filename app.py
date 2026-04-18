import streamlit as st

# Configuración de la página (Mobile-First)
st.set_page_config(
    page_title="RRHH - Reclutamiento y ADP",
    layout="centered",
    initial_sidebar_state="auto"
)

# Navegación en la barra lateral
st.sidebar.title("Navegación")
seccion = st.sidebar.radio(
    "Selecciona una sección:",
    ["1. El Reclutamiento", "2. El ADP", "3. Técnicas de Recogida"]
)

if seccion == "1. El Reclutamiento":
    # Contenido de la Sección 1
    st.markdown("""
# 1. El Reclutamiento: Planificación y Captación de Talento

El Reclutamiento no es una función administrativa aislada, sino el proceso técnico de prospección para captar talento cuando la plantilla actual es insuficiente para cubrir las necesidades futuras de la organización.

## 1.1. Planificación Estratégica
Antes de buscar candidatos, es vital planificar la captación basándose en dos pilares:

*   **Gestión del tiempo:** Necesitaremos más tiempo de antelación cuanto mayor sea la escasez de personal cualificado en el mercado de trabajo.
*   **Viabilidad Financiera:** Partiendo únicamente de la necesidad neta de personal no sabremos si podemos permitirnos esa plantilla. Es necesario calcular los costes de personal para el período planificado. Esto incluye sueldos brutos, pluses, horas extras y las cotizaciones a la Seguridad Social (por ejemplo, las Contingencias Comunes suponen un 23,60% a cargo de la empresa). La informática nos ayuda a realizar simulaciones del tipo "qué-hubiera-pasado-si..." para evaluar diferentes escenarios.

## 1.2. Estrategias de Captación: Reclutamiento Interno
Buscar trabajadores dentro de la propia empresa fomenta la motivación. Existen dos caminos principales:

*   **Vía Directa:** Convocar de forma oficial la plaza a ocupar para que los trabajadores presenten su solicitud, o dirigirse directamente a un trabajador para plantearle el cambio.
*   **Vía Indirecta:** Averiguar, mediante valoraciones periódicas, el potencial de los trabajadores para ocupar otros puestos. Para esto, la valoración de los puestos de trabajo debe ser aceptada por todos los empleados a los que afecte.

💡 **Alternativas previas:** A veces no es necesario contratar. A corto plazo se pueden usar horas extras. A medio y largo plazo, reducir el absentismo o mejorar los recursos técnicos permite trabajar de forma más productiva, reduciendo la necesidad de nuevas contrataciones.

## 1.3. Estrategias de Captación: Reclutamiento Externo
Cuando se acude al mercado de trabajo exterior, existen diversas tácticas:

*   **Intermediarios y Networking:** Consultar bolsas de empleo, agencias locales (INEM), o recurrir a empresas de trabajo temporal (ETT) y consultoras para cubrir puestos de manera inmediata. Además, implicar a los trabajadores actuales mediante el "boca a boca" resulta un recurso económico y muy eficaz.
*   **El Anuncio de Empleo:** Al publicar una oferta, no solo debemos proporcionar información objetiva, sino también incluir aspectos sobre la manera de trabajar en la empresa (cultura organizacional). Es imperativo mantener la obligación de neutralidad respecto de ambos sexos. Como buena práctica, se aconseja consultar con el equipo actual el boceto de la oferta para dirigirse mejor al grupo objetivo.
""")

    st.markdown("---")
    st.header("Autoevaluación")
    st.write("Pon a prueba tus conocimientos sobre la planificación y captación de talento.")

    with st.form("quiz_form"):
        q1 = st.radio(
            "1. Según la planificación de la contratación, ¿qué factor nos obliga a preparar el reclutamiento con mayor tiempo de antelación?",
            options=["A) El cálculo de las contingencias comunes", 
                     "B) La escasez de personal cualificado en el mercado", 
                     "C) El número de horas extras permitidas", 
                     "D) El uso de redes sociales"],
            index=None
        )
        
        q2 = st.radio(
            "2. ¿Qué herramienta es la base para el 'camino indirecto' en el reclutamiento interno?",
            options=["A) Las ETTs", 
                     "B) La convocatoria oficial de plaza", 
                     "C) La valoración periódica de los puestos de trabajo", 
                     "D) El anuncio de empleo neutral"],
            index=None
        )

        q3 = st.radio(
            "3. En el cálculo de los costes operativos para comprobar la viabilidad financiera, ¿qué porcentaje aproximado suelen suponer las Contingencias Comunes a cargo de la empresa?",
            options=["A) 6,00%", "B) 7,70%", "C) 14,00%", "D) 23,60%"],
            index=None
        )

        q4 = st.radio(
            "4. ¿Cuál de los siguientes NO es un método de reclutamiento externo?",
            options=["A) Colaboración con oficinas del INEM", 
                     "B) Consultoras de reclutamiento", 
                     "C) Promoción directa de un subordinado", 
                     "D) Networking o 'boca a boca'"],
            index=None
        )

        q5 = st.radio(
            "5. A la hora de redactar un anuncio de empleo externo, ¿qué dualidad informativa debe cumplir?",
            options=["A) Información objetiva de tareas + cultura organizacional", 
                     "B) Salario bruto + salario neto", 
                     "C) Horario + Contingencias comunes", 
                     "D) Neutralidad legal + Listado de horas extras"],
            index=None
        )

        submitted = st.form_submit_button("Comprobar Respuestas")

    if submitted:
        st.subheader("Resultados")
        
        # Pregunta 1
        if q1 and q1.startswith("B"):
            st.success("Pregunta 1: Correcto. La escasez de perfiles cualificados en el mercado laboral exige iniciar la búsqueda mucho antes para garantizar el éxito.")
        else:
            st.error("Pregunta 1: Incorrecto. La escasez de perfiles cualificados en el mercado laboral exige iniciar la búsqueda mucho antes para garantizar el éxito.")
            
        # Pregunta 2
        if q2 and q2.startswith("C"):
            st.success("Pregunta 2: Correcto. El camino indirecto busca detectar el potencial latente de los trabajadores actuales mediante la Valoración de Puestos de Trabajo (VPT).")
        else:
            st.error("Pregunta 2: Incorrecto. El camino indirecto busca detectar el potencial latente de los trabajadores actuales mediante la Valoración de Puestos de Trabajo (VPT).")
            
        # Pregunta 3
        if q3 and q3.startswith("D"):
            st.success("Pregunta 3: Correcto. Las Contingencias Comunes son el mayor porcentaje, suponiendo habitualmente un 23,60%.")
        else:
            st.error("Pregunta 3: Incorrecto. Las Contingencias Comunes son el mayor porcentaje, suponiendo habitualmente un 23,60%.")
            
        # Pregunta 4
        if q4 and q4.startswith("C"):
            st.success("Pregunta 4: Correcto. La promoción directa es un método de reclutamiento interno.")
        else:
            st.error("Pregunta 4: Incorrecto. La promoción directa es un método de reclutamiento interno.")
            
        # Pregunta 5
        if q5 and q5.startswith("A"):
            st.success("Pregunta 5: Correcto. El anuncio debe incluir la información objetiva de las tareas, pero también proyectar la cultura de la empresa (ej. ambiente de trabajo).")
        else:
            st.error("Pregunta 5: Incorrecto. El anuncio debe incluir la información objetiva de las tareas, pero también proyectar la cultura de la empresa (ej. ambiente de trabajo).")

elif seccion == "2. El ADP":
    st.title("2. El ADP: Análisis y Descripción de Puestos")

    st.header("2.1. Fundamentos y Evolución")
    st.write("El ADP es el eje de la organización científica del trabajo. Ha evolucionado desde la simple clasificación de tareas (Taylorismo) hasta ser un instrumento estratégico de gestión por competencias.")
    st.info("🎯 **Enfoque:** Se analiza el trabajo en sí mismo, no a la persona que lo desempeña.")

    st.header("2.2. El Trípode del Puesto")
    st.write("Todo puesto se define por la interacción de tres elementos:")
    with st.container():
        st.markdown("🛠️ **Tareas:** Qué acciones realiza el trabajador (ej. el pintor lija y prepara la superficie).")
        st.markdown("⚖️ **Responsabilidades:** Compromisos y toma de decisiones (ej. asegurar la satisfacción del cliente).")
        st.markdown("🧠 **Competencias:** Conocimientos y habilidades necesarias (ej. formación técnica en automoción).")

    st.header("2.3. Utilidad Estratégica y Salud Laboral")
    st.write("El ADP no es solo \"papeleo\", es la base para:")
    with st.container():
        st.info("✅ **Selección y Formación:** Define el perfil ideal y detecta qué formación falta.")
        st.info("🛡️ **Prevención de Riesgos:** Identifica peligros ergonómicos, físicos y psicosociales para adaptar el puesto al trabajador.")

    st.header("2.4. El Análisis Operativo (Las 5 Preguntas)")
    st.write("Para describir un puesto con rigor, debemos responder:")
    with st.container():
        st.markdown("🔹 **¿Qué hace?** (Tareas y funciones)")
        st.markdown("🔹 **¿Cómo lo hace?** (Métodos y procedimientos)")
        st.markdown("🔹 **¿Con qué lo hace?** (Herramientas y maquinaria)")
        st.markdown("🔹 **¿Por qué lo hace?** (Misión y finalidad)")
        st.markdown("🔹 **¿Quién lo hace?** (Requisitos y aptitudes humanas)")

elif seccion == "3. Técnicas de Recogida":
    st.header("3. Técnicas de Recogida")
    st.info("Contenido en desarrollo. Próximamente se añadirán los conceptos teóricos.")
