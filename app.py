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
    ["1. El Reclutamiento", "2. El ADP", "3. Dimensión Económica", "4. Técnicas de Recogida", "5. Metodología y Estrategia"]
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
    st.title("2. EL ADP: Análisis y Descripción de Puestos")

    st.header("2.1. Contexto Histórico y Evolución")
    st.write("El origen del ADP se remonta a la organización científica del trabajo (fines del s. XIX). Autores como Frederick Taylor introdujeron la idea de desglosar el trabajo en tareas cuantificables para mejorar la eficiencia. Posteriormente, la escuela de las relaciones humanas integró el factor humano. Además, los periodos de guerra (I y II Guerra Mundial) obligaron a desarrollar métodos sistemáticos de estandarización de puestos por la escasez de recursos. Hoy en día, el ADP ha pasado de ser una herramienta puramente administrativa a un instrumento estratégico central en RR.HH.")

    st.header("2.2. Definiciones Clave")
    st.write("El ADP es un proceso sistemático de recogida, análisis y organización de información relativa a un puesto de trabajo con el objetivo de identificar sus funciones, responsabilidades y requisitos.")
    st.info("Es una técnica centrada exclusivamente en el puesto y no en la persona. Se analiza el trabajo en sí mismo, independientemente de quién lo ocupe. Su resultado principal es la \"descripción del puesto\".")

    st.header("2.3. El Trípode del Puesto")
    st.write("El análisis se apoya en tres pilares fundamentales que estructuran la información:")
    with st.container():
        st.markdown("* **Tareas:** Conjunto de actividades concretas, observables y medibles. Se debe identificar su frecuencia, dificultad y peso en la jornada.")
        st.markdown("* **Responsabilidades:** Obligaciones asociadas al puesto que determinan el nivel de compromiso, autonomía y toma de decisiones (grado de autoridad).")
        st.markdown("* **Competencias:** Conjunto de conocimientos (saber), habilidades (saber hacer) y actitudes (transversales) necesarias para ejecutar las tareas.")

    st.markdown("---")
    st.header("Autoevaluación")
    st.write("Pon a prueba tus conocimientos sobre el Análisis y Descripción de Puestos.")

    with st.form("form_adp"):
        q1_adp = st.radio(
            "1. ¿Qué factores históricos impulsaron el desarrollo de métodos sistemáticos de estandarización de puestos?",
            options=[
                "A) La necesidad de organizar la mano de obra durante los periodos de las guerras mundiales",
                "B) La invención de la computadora",
                "C) Las demandas sindicales a finales del s. XIX",
                "D) El auge de las redes sociales corporativas"
            ],
            index=None
        )

        q2_adp = st.radio(
            "2. ¿En qué se centra principalmente la técnica del ADP?",
            options=[
                "A) En la motivación de la persona que ocupa el cargo",
                "B) Exclusivamente en el puesto de trabajo, independientemente de la persona que lo ocupe",
                "C) En calcular las horas extras del departamento",
                "D) En organizar eventos de la empresa"
            ],
            index=None
        )

        q3_adp = st.radio(
            "3. Dentro del trípode del puesto, ¿qué elemento define el nivel de autonomía y la toma de decisiones?",
            options=[
                "A) Las tareas",
                "B) Las competencias",
                "C) Las responsabilidades",
                "D) La experiencia previa"
            ],
            index=None
        )

        submitted_adp = st.form_submit_button("Comprobar Respuestas")

    if submitted_adp:
        st.subheader("Resultados")

        # Pregunta 1
        if q1_adp and q1_adp.startswith("A"):
            st.success("Pregunta 1: Correcto. La necesidad de organizar la mano de obra durante los periodos de las guerras mundiales.")
        else:
            st.error("Pregunta 1: Incorrecto. Relee la parte de las guerras mundiales, donde la escasez exigió obligadamente la organización.")

        # Pregunta 2
        if q2_adp and q2_adp.startswith("B"):
            st.success("Pregunta 2: Correcto. Exclusivamente en el puesto de trabajo, independientemente de la persona que lo ocupe.")
        else:
            st.error("Pregunta 2: Incorrecto. El ADP se centra de forma exclusiva en el puesto de trabajo.")

        # Pregunta 3
        if q3_adp and q3_adp.startswith("C"):
            st.success("Pregunta 3: Correcto. Las responsabilidades definen el grado de autonomía para tomar decisiones.")
        else:
            st.error("Pregunta 3: Incorrecto. Las responsabilidades son la respuesta adecuada referida al nivel de compromiso.")

elif seccion == "3. Dimensión Económica":
    st.title("3. Dimensión Económica del Personal")

    st.write("Contratar no es únicamente encontrar a la persona adecuada, sino asegurar que la empresa puede asumir ese coste mes a mes sin desestabilizar su estructura financiera. La planificación del personal siempre debe aterrizar en un presupuesto y en un cálculo del coste por hora.")

    st.header("3.1. El Presupuesto como Herramienta de Control")
    st.write("Saber cuántas personas hacen falta no garantiza que la empresa pueda pagarlas. El presupuesto traduce el plan de plantilla a cifras y tiene una doble función:")
    st.markdown("1. **Viabilidad:** Comprueba si la empresa puede permitirse la contratación.")
    st.markdown("2. **Seguimiento:** Detecta desviaciones mensuales antes de que sean un problema.")

    st.info("**Análisis de Sensibilidad:** Al usar hojas de cálculo con fórmulas cerradas, el presupuesto permite plantear escenarios como \"¿cuánto ahorraríamos si transformásemos dos contratos temporales en uno indefinido?\". Además, es útil imputar los costes por *centro de coste* (comercial, producción, etc.) para delegar la responsabilidad del gasto en los mandos intermedios.")

    st.header("3.2. Cotizaciones a la Seguridad Social")
    st.write("El empresario no paga solo el salario bruto, sino también una cuota a la Seguridad Social que puede elevar el coste total por encima del 30% del salario. El grueso de este coste recae de forma muy desigual sobre la empresa.")

    st.markdown("""
| Concepto | Empresa (%) | Trabajador (%) | Total (%) |
| :--- | :--- | :--- | :--- |
| Contingencias Comunes | 23,60% | 4,70% | 28,30% |
| Desempleo (Indefinido) | 6,00% | 1,55% | 7,55% |
| Desempleo (Temporal/ETT) | 7,70% | 1,60% | 9,30% |
| FOGASA | 0,40% | - | 0,40% |
""")

    st.warning("**El epígrafe de accidentes (AT y EP):** Es un coste variable a cargo exclusivo de la empresa que depende de la actividad. No cuesta lo mismo asegurar a un administrativo que a un operario de obra.")

    st.header("3.3. Complementos Salariales y Horas")
    st.write("La mayoría de los pluses (peligrosidad, nocturnidad) se suman al salario bruto y *elevan la base de cotización* (se paga más a la Seguridad Social).")

    st.markdown("""
* **La excepción - El Plus de Transporte:** Compensa el gasto de desplazamiento, no el trabajo. Por tanto, *no computa* en la base de cotización siempre que esté dentro del límite legal.
* **Horas Extraordinarias:** Las justificadas por *fuerza mayor* cotizan muy bajo (14% conjunto). El resto de horas extras cotizan igual que las contingencias comunes (28,30% conjunto). Abusar de ellas encarece la factura rápidamente.
* **Horas Complementarias:** Solo aplican a contratos a tiempo parcial. Se retribuyen y cotizan exactamente igual que una hora ordinaria.
""")

    st.header("3.4. Cálculo del Coste Hora")
    st.write("Para obtener una cifra operativa, la empresa debe sumar el salario bruto más todas las cotizaciones a su cargo para obtener el **Coste Total Empresa**.")
    st.write("Para hallar el coste por hora real, se divide ese coste total entre el número de horas que marca el convenio.")

    st.markdown("---")
    st.header("Autoevaluación")
    st.write("Pon a prueba tus conocimientos sobre la Dimensión Económica.")

    with st.form("quiz_econ"):
        q1_econ = st.radio(
            "1. ¿Cuál es el concepto de cotización que supone el mayor coste para la empresa y qué porcentaje habitual representa?",
            options=[
                "A) Desempleo Indefinido, un 7,55%",
                "B) Desempleo Temporal, un 9,30%",
                "C) Contingencias comunes, un 23,60% a cargo de la empresa",
                "D) FOGASA, un 0,40%"
            ],
            index=None
        )

        q2_econ = st.radio(
            "2. ¿Qué característica especial tiene el \"Plus de Transporte\" frente a otros pluses como el de nocturnidad?",
            options=[
                "A) Siempre cotiza el doble a la Seguridad Social.",
                "B) Solo se paga a los contratos a tiempo parcial.",
                "C) Debe pagarse siempre en efectivo y en mano.",
                "D) No se considera pago por trabajo, por lo que no computa en la base de cotización de la Seguridad Social hasta el límite legal."
            ],
            index=None
        )

        q3_econ = st.radio(
            "3. ¿A qué tipo de contrato se aplican las \"Horas Complementarias\" y cómo cotizan?",
            options=[
                "A) Se aplican a contratos a tiempo parcial y cotizan igual que el salario ordinario.",
                "B) Solo a directivos y no cotizan.",
                "C) A contratos temporales y cotizan más barato que las horas extra.",
                "D) A contratos de formación exclusivamente."
            ],
            index=None
        )

        q4_econ = st.radio(
            "4. En la gestión del presupuesto, ¿qué es el \"análisis de sensibilidad\"?",
            options=[
                "A) Analizar psicológicamente a los empleados para medir su estrés.",
                "B) La capacidad de usar herramientas informáticas para plantear escenarios del tipo \"¿qué pasaría si...?\" y evaluar el impacto económico.",
                "C) Evaluar el riesgo de impago de un cliente.",
                "D) Una métrica para medir las quejas sindicales."
            ],
            index=None
        )

        submitted_econ = st.form_submit_button("Comprobar Respuestas")

    if submitted_econ:
        st.subheader("Resultados")

        # Pregunta 1
        if q1_econ and q1_econ.startswith("C"):
            st.success("Pregunta 1: Correcto. Las Contingencias Comunes son la principal partida y suponen un 23,60% con cargo a la empresa.")
        else:
            st.error("Pregunta 1: Incorrecto. Revisa la tabla de cotizaciones, la partida más grande son las Contingencias Comunes.")

        # Pregunta 2
        if q2_econ and q2_econ.startswith("D"):
            st.success("Pregunta 2: Correcto. El Plus de Transporte compensa el desplazamiento, no es estricto salario por trabajar, y puede estar exento si respeta los límites legales.")
        else:
            st.error("Pregunta 2: Incorrecto. Recuerda que es un concepto que compensa desplazamiento, por lo que tiene ventajas de cotización.")

        # Pregunta 3
        if q3_econ and q3_econ.startswith("A"):
            st.success("Pregunta 3: Correcto. Se aplican solo a parciales y su precio y cotización es igual que el de una hora normal.")
        else:
            st.error("Pregunta 3: Incorrecto. Las horas complementarias son específicas del trabajo a tiempo parcial y no se penalizan con más porcentaje.")

        # Pregunta 4
        if q4_econ and q4_econ.startswith("B"):
            st.success("Pregunta 4: Correcto. Nos permite adelantarnos a posibles sobrecostes jugando con distintas variables.")
        else:
            st.error("Pregunta 4: Incorrecto. Tiene que ver con las hipótesis y escenarios presupuestarios en hojas de cálculo.")

elif seccion == "4. Técnicas de Recogida":
    st.title("4. Técnicas de Recogida")
    st.info("Contenido en desarrollo. Próximamente se añadirán los conceptos teóricos.")

elif seccion == "5. Metodología y Estrategia":
    st.title("5. Metodología y Estrategia")

    st.header("5.1. Importancia Estratégica del ADP")
    st.write("El ADP es la \"pieza maestra\" de la organización.")
    with st.container():
        st.info("🎯 **Selección:** Crea el profesiograma (perfil ideal).")
        st.info("📚 **Formación:** Detecta \"lagunas\" de conocimiento comparando el perfil real con la exigencia del puesto.")
        st.info("⚖️ **Responsabilidades:** Delimita autoridad y evita la ambigüedad de rol.")

    st.header("5.2. Salud Laboral y Prevención")
    st.write("El ADP es la base técnica para la seguridad del trabajador:")
    with st.container():
        st.markdown("- 🛡️ **Seguridad e Higiene:** Control de equipos y agentes químicos/físicos.")
        st.markdown("- 🧘 **Ergonomía y Psicosociología:** Control de fatiga, estrés y posturas.")
        st.markdown("- 🩺 **Medicina del Trabajo:** Vigilancia de la salud según el riesgo del puesto.")
        st.success("✅ **Acción Preventiva:** \"Adaptar el trabajo a la persona\".")

    st.header("5.3. Análisis Operativo: Las 5 Cuestiones")
    st.write("Todo análisis debe responder con rigor a:")
    with st.container():
        st.markdown("🔹 **¿Qué hace?** (Tareas y tiempo).")
        st.markdown("🔹 **¿Cómo lo hace?** (Métodos y riesgos).")
        st.markdown("🔹 **¿Con qué lo hace?** (Recursos y herramientas).")
        st.markdown("🔹 **¿Por qué lo hace?** (Misión y objetivo).")
        st.markdown("🔹 **¿Quién lo hace?** (Aptitudes y formación).")

    st.header("5.4. Participantes y Selección de Puestos")
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
