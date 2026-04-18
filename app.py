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
    ["1. El Reclutamiento", "2. El ADP", "3. Técnicas de Recogida", "4. Metodología y Estrategia"]
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

    st.markdown("---")
    st.header("Autoevaluación")
    st.write("Pon a prueba tus conocimientos sobre el Análisis y Descripción de Puestos.")

    with st.form("form_adp"):
        q1_adp = st.radio(
            "1. El Análisis y Descripción de Puestos (ADP) se caracteriza principalmente por centrarse en:",
            options=[
                "A) La persona que ocupa el cargo actualmente",
                "B) El puesto de trabajo en sí mismo independientemente de quién lo ocupe",
                "C) El cálculo de las horas extras",
                "D) La evaluación del desempeño del empleado"
            ],
            index=None
        )

        q2_adp = st.radio(
            "2. Dentro del \"Trípode del Puesto\", ¿qué elemento define las obligaciones y el nivel de compromiso (por ejemplo, \"garantizar la satisfacción del cliente\")?",
            options=[
                "A) Las Tareas",
                "B) Las Competencias",
                "C) Las Responsabilidades",
                "D) Los Riesgos Laborales"
            ],
            index=None
        )

        q3_adp = st.radio(
            "3. En el ámbito de la Salud y Seguridad Laboral, el ADP es fundamental porque permite:",
            options=[
                "A) Identificar riesgos físicos, ergonómicos y psicosociales para adaptar el trabajo a la persona",
                "B) Reducir el sueldo si el puesto es peligroso",
                "C) Evitar el pago de cotizaciones a la Seguridad Social",
                "D) Contratar a trabajadores sin experiencia médica"
            ],
            index=None
        )

        q4_adp = st.radio(
            "4. Según el Análisis Operativo, si documentamos que el pintor \"realiza la mezcla de colores utilizando una máquina específica y un ordenador\", ¿a qué pregunta estamos respondiendo?",
            options=[
                "A) ¿Qué hace?",
                "B) ¿Por qué lo hace?",
                "C) ¿Cómo lo hace?",
                "D) ¿Quién lo hace?"
            ],
            index=None
        )

        q5_adp = st.radio(
            "5. La pregunta \"¿Quién lo hace?\" en las 5 cuestiones básicas del ADP se refiere a:",
            options=[
                "A) El nombre del trabajador actual",
                "B) El departamento al que pertenece",
                "C) Los recursos materiales empleados",
                "D) Los requisitos humanos en términos de formación y aptitudes"
            ],
            index=None
        )

        submitted_adp = st.form_submit_button("Comprobar Respuestas")

    if submitted_adp:
        st.subheader("Resultados")

        # Pregunta 1
        if q1_adp and q1_adp.startswith("B"):
            st.success("Pregunta 1: Correcto. El ADP es una técnica que analiza la naturaleza del trabajo y sus requisitos, no a la persona concreta que lo está desempeñando.")
        else:
            st.error("Pregunta 1: Incorrecto. El ADP es una técnica que analiza la naturaleza del trabajo y sus requisitos, no a la persona concreta que lo está desempeñando.")

        # Pregunta 2
        if q2_adp and q2_adp.startswith("C"):
            st.success("Pregunta 2: Correcto. Las responsabilidades son las obligaciones asociadas al puesto que determinan el nivel de compromiso y la toma de decisiones.")
        else:
            st.error("Pregunta 2: Incorrecto. Las responsabilidades son las obligaciones asociadas al puesto que determinan el nivel de compromiso y la toma de decisiones.")

        # Pregunta 3
        if q3_adp and q3_adp.startswith("A"):
            st.success("Pregunta 3: Correcto. Al analizar detalladamente las tareas y el entorno, el ADP detecta los riesgos reales, permitiendo diseñar medidas preventivas eficaces.")
        else:
            st.error("Pregunta 3: Incorrecto. Al analizar detalladamente las tareas y el entorno, el ADP detecta los riesgos reales, permitiendo diseñar medidas preventivas eficaces.")

        # Pregunta 4
        if q4_adp and q4_adp.startswith("C"):
            st.success("Pregunta 4: Correcto. La pregunta '¿Cómo lo hace?' describe los procedimientos, instrucciones y métodos técnicos utilizados en el trabajo.")
        else:
            st.error("Pregunta 4: Incorrecto. La pregunta '¿Cómo lo hace?' describe los procedimientos, instrucciones y métodos técnicos utilizados en el trabajo.")

        # Pregunta 5
        if q5_adp and q5_adp.startswith("D"):
            st.success("Pregunta 5: Correcto. El 'Quién' se centra en definir el perfil ideal, detallando las capacidades, formación técnica (ej. FP Automoción) y habilidades necesarias para el cargo.")
        else:
            st.error("Pregunta 5: Incorrecto. El 'Quién' se centra en definir el perfil ideal, detallando las capacidades, formación técnica (ej. FP Automoción) y habilidades necesarias para el cargo.")

elif seccion == "3. Técnicas de Recogida":
    st.header("3. Técnicas de Recogida")
    st.info("Contenido en desarrollo. Próximamente se añadirán los conceptos teóricos.")

elif seccion == "4. Metodología y Estrategia":
    st.title("4. Metodología y Estrategia")

    st.header("4.1. Importancia Estratégica del ADP")
    st.write("El ADP es la \"pieza maestra\" de la organización.")
    with st.container():
        st.info("🎯 **Selección:** Crea el profesiograma (perfil ideal).")
        st.info("📚 **Formación:** Detecta \"lagunas\" de conocimiento comparando el perfil real con la exigencia del puesto.")
        st.info("⚖️ **Responsabilidades:** Delimita autoridad y evita la ambigüedad de rol.")

    st.header("4.2. Salud Laboral y Prevención")
    st.write("El ADP es la base técnica para la seguridad del trabajador:")
    with st.container():
        st.markdown("- 🛡️ **Seguridad e Higiene:** Control de equipos y agentes químicos/físicos.")
        st.markdown("- 🧘 **Ergonomía y Psicosociología:** Control de fatiga, estrés y posturas.")
        st.markdown("- 🩺 **Medicina del Trabajo:** Vigilancia de la salud según el riesgo del puesto.")
        st.success("✅ **Acción Preventiva:** \"Adaptar el trabajo a la persona\".")

    st.header("4.3. Análisis Operativo: Las 5 Cuestiones")
    st.write("Todo análisis debe responder con rigor a:")
    with st.container():
        st.markdown("🔹 **¿Qué hace?** (Tareas y tiempo).")
        st.markdown("🔹 **¿Cómo lo hace?** (Métodos y riesgos).")
        st.markdown("🔹 **¿Con qué lo hace?** (Recursos y herramientas).")
        st.markdown("🔹 **¿Por qué lo hace?** (Misión y objetivo).")
        st.markdown("🔹 **¿Quién lo hace?** (Aptitudes y formación).")

    st.header("4.4. Participantes y Selección de Puestos")
    with st.container():
        st.markdown("👥 **Actores:** El Analista, el Titular del puesto, el Superior Jerárquico y RR.HH.")
        st.info("📊 **Criterio de Selección:** Representatividad. No se analiza todo, sino puestos \"tipo\" significativos.")
        st.markdown("🔍 **Identificación:** Se puede validar mediante registros de RR.HH., consulta a jefes, encuestas a empleados o investigación exhaustiva.")

    st.markdown("---")
    st.header("Autoevaluación")
    st.write("Pon a prueba tus conocimientos sobre Metodología y Estrategia del ADP.")

    with st.form("form_metodologia"):
        q1_met = st.radio(
            "1. A nivel estratégico, ¿cómo se vincula el Análisis de Puestos (ADP) con los planes de Formación de la empresa?",
            options=[
                "A) Permite reducir el salario de los empleados menos formados",
                "B) Detecta \"lagunas\" de conocimiento al comparar el perfil real del trabajador con las exigencias del puesto",
                "C) Sustituye por completo a la evaluación del desempeño",
                "D) Sirve únicamente para cumplir requisitos legales"
            ],
            index=None
        )

        q2_met = st.radio(
            "2. Según los Principios de la Acción Preventiva en Salud Laboral, el enfoque fundamental a la hora de diseñar un puesto de trabajo es:",
            options=[
                "A) Adaptar el trabajo a la persona",
                "B) Adaptar a la persona al trabajo cueste lo que cueste",
                "C) Pagar pluses de peligrosidad en lugar de modificar las máquinas",
                "D) Delegar la responsabilidad en las Mutuas externas"
            ],
            index=None
        )

        q3_met = st.radio(
            "3. Si en el análisis de un puesto detectamos riesgos derivados de \"posturas forzadas, fatiga mental y estrés\", ¿a qué especialidad preventiva estamos nutriendo de datos?",
            options=[
                "A) Seguridad en el Trabajo",
                "B) Higiene Ocupacional",
                "C) Medicina del Trabajo",
                "D) Psicosociología y Ergonomía"
            ],
            index=None
        )

        q4_met = st.radio(
            "4. En el Análisis Operativo, si el analista documenta las \"aptitudes físicas, conocimientos técnicos y capacidades mentales necesarias\" para ser pintor, ¿a qué pregunta básica está respondiendo?",
            options=[
                "A) ¿Qué hace?",
                "B) ¿Cómo lo hace?",
                "C) ¿Con qué lo hace?",
                "D) ¿Quién lo hace?"
            ],
            index=None
        )

        q5_met = st.radio(
            "5. En organizaciones muy grandes donde es inviable analizar puesto por puesto, ¿cuál es el criterio principal para seleccionar los puestos que se van a estudiar?",
            options=[
                "A) Criterio de aleatoriedad",
                "B) Criterio de representatividad (elegir puestos \"tipo\" significativos)",
                "C) Analizar solo los puestos directivos",
                "D) Analizar los puestos que más quejas generan"
            ],
            index=None
        )

        submitted_met = st.form_submit_button("Comprobar Respuestas")

    if submitted_met:
        st.subheader("Resultados")

        # Pregunta 1
        if q1_met and q1_met.startswith("B"):
            st.success("Pregunta 1: Correcto. El ADP define lo que el puesto exige, y al cruzarlo con lo que el trabajador sabe, identificamos exactamente en qué debemos capacitarle de forma rentable.")
        else:
            st.error("Pregunta 1: Incorrecto. El ADP define lo que el puesto exige, y al cruzarlo con lo que el trabajador sabe, identificamos exactamente en qué debemos capacitarle de forma rentable.")

        # Pregunta 2
        if q2_met and q2_met.startswith("A"):
            st.success("Pregunta 2: Correcto. La Ley exige que, en la medida de lo posible, el entorno, los equipos y el diseño del puesto se adapten a la persona para evitar o minimizar los riesgos.")
        else:
            st.error("Pregunta 2: Incorrecto. La Ley exige que, en la medida de lo posible, el entorno, los equipos y el diseño del puesto se adapten a la persona para evitar o minimizar los riesgos.")

        # Pregunta 3
        if q3_met and q3_met.startswith("D"):
            st.success("Pregunta 3: Correcto. La ergonomía trata la carga física y las posturas, mientras que la psicosociología aborda factores organizativos como el estrés o la fatiga mental.")
        else:
            st.error("Pregunta 3: Incorrecto. La ergonomía trata la carga física y las posturas, mientras que la psicosociología aborda factores organizativos como el estrés o la fatiga mental.")

        # Pregunta 4
        if q4_met and q4_met.startswith("D"):
            st.success("Pregunta 4: Correcto. La pregunta '¿Quién lo hace?' se centra exclusivamente en los requisitos humanos y el perfil ideal que debe tener la persona que ocupe el cargo.")
        else:
            st.error("Pregunta 4: Incorrecto. La pregunta '¿Quién lo hace?' se centra exclusivamente en los requisitos humanos y el perfil ideal que debe tener la persona que ocupe el cargo.")

        # Pregunta 5
        if q5_met and q5_met.startswith("B"):
            st.success("Pregunta 5: Correcto. Se selecciona un puesto que represente a muchos otros idénticos (por ejemplo, analizar a un pintor para establecer el estándar de los 20 pintores de la plantilla).")
        else:
            st.error("Pregunta 5: Incorrecto. Se selecciona un puesto que represente a muchos otros idénticos (por ejemplo, analizar a un pintor para establecer el estándar de los 20 pintores de la plantilla).")
