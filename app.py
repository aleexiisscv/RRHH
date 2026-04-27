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

    with st.form("quiz_reclutamiento"):
        q1 = st.radio(
            "1. ¿Qué es el reclutamiento en el contexto organizativo?",
            options=[
                "A) Una función administrativa independiente del resto", 
                "B) Un proceso técnico para atraer candidatos cualificados", 
                "C) Un método para reducir costes laborales"
            ],
            index=None
        )
        
        q2 = st.radio(
            "2. ¿En qué se basa la decisión entre reclutamiento interno, externo o mixto?",
            options=[
                "A) En la antigüedad de los empleados", 
                "B) En un análisis de coste-beneficio", 
                "C) En la preferencia del departamento de RRHH"
            ],
            index=None
        )

        q3 = st.radio(
            "3. ¿Cuándo surge la planificación de la captación de personal?",
            options=[
                "A) Cuando hay exceso de trabajadores", 
                "B) Cuando el número de trabajadores actuales es inferior al plan futuro", 
                "C) Cuando se reducen los beneficios empresariales"
            ],
            index=None
        )

        q4 = st.radio(
            "4. ¿Qué caracteriza al reclutamiento interno por vía indirecta?",
            options=[
                "A) La publicación de una convocatoria oficial", 
                "B) La contratación a través de agencias externas", 
                "C) La detección del potencial de los trabajadores mediante evaluaciones periódicas"
            ],
            index=None
        )

        q5 = st.radio(
            "5. ¿Cuál es un requisito fundamental en el diseño de un anuncio de empleo?",
            options=[
                "A) Incluir únicamente información sobre el salario", 
                "B) Mantener la neutralidad legal y evitar discriminación", 
                "C) Priorizar siempre el uso de redes sociales"
            ],
            index=None
        )

        q6 = st.radio(
            "6. ¿Qué ventaja principal ofrece el uso de 'Redes de Contacto' (Networking o 'boca a boca') como táctica de reclutamiento externo?",
            options=[
                "A) Permite delegar la fase de criba técnica a consultoras especializadas", 
                "B) Es un recurso económico que suele ofrecer resultados de alta fidelidad", 
                "C) Atrae exclusivamente a candidatos de alta cualificación académica sin experiencia previa"
            ],
            index=None
        )

        submitted = st.form_submit_button("Comprobar Respuestas")

    if submitted:
        st.subheader("Resultados")
        
        if q1 and q1.startswith("B"): st.success("Pregunta 1: ¡Correcto!") 
        else: st.error("Pregunta 1: Incorrecto. Es un proceso técnico para atraer candidatos cualificados.")
            
        if q2 and q2.startswith("B"): st.success("Pregunta 2: ¡Correcto!") 
        else: st.error("Pregunta 2: Incorrecto. Se basa en un análisis de coste-beneficio.")
            
        if q3 and q3.startswith("B"): st.success("Pregunta 3: ¡Correcto!") 
        else: st.error("Pregunta 3: Incorrecto. Surge cuando el número de trabajadores actuales es inferior al plan futuro.")
            
        if q4 and q4.startswith("C"): st.success("Pregunta 4: ¡Correcto!") 
        else: st.error("Pregunta 4: Incorrecto. Se basa en la detección del potencial mediante evaluaciones periódicas.")
            
        if q5 and q5.startswith("B"): st.success("Pregunta 5: ¡Correcto!") 
        else: st.error("Pregunta 5: Incorrecto. Es fundamental mantener la neutralidad legal y evitar discriminación.")

        if q6 and q6.startswith("B"): st.success("Pregunta 6: ¡Correcto!") 
        else: st.error("Pregunta 6: Incorrecto. Es un recurso económico que suele ofrecer resultados de alta fidelidad.")

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
    st.write("Pon a prueba tus conocimientos sobre los fundamentos, evolución y estructura del ADP.")

    with st.form("quiz_adp_definitivo"):
        q1 = st.radio(
            "1. ¿Qué elementos conforman las 'Competencias' dentro del denominado 'Trípode del Puesto' en el ADP?",
            options=[
                "A) El conjunto de conocimientos, habilidades y actitudes necesarias para ejecutar correctamente las tareas", 
                "B) Las obligaciones asociadas al puesto que determinan el nivel de autonomía, compromiso y autoridad", 
                "C) La enumeración de las actividades físicas observables, la maquinaria y las herramientas proporcionadas"
            ],
            index=None
        )
        
        q2 = st.radio(
            "2. ¿Cuál es el objetivo principal del Análisis y Descripción de Puestos (ADP)?",
            options=[
                "A) Reducir los costes salariales de la empresa", 
                "B) Ofrecer una estructura objetiva para comprender y optimizar los puestos", 
                "C) Sustituir a los trabajadores por tecnología"
            ],
            index=None
        )

        q3 = st.radio(
            "3. En sus primeras aplicaciones, el ADP se utilizaba principalmente para:",
            options=[
                "A) La evaluación del desempeño", 
                "B) La clasificación de tareas y la asignación salarial", 
                "C) La prevención de riesgos laborales"
            ],
            index=None
        )

        q4 = st.radio(
            "4. ¿Cómo se considera actualmente el ADP dentro de la gestión de RR.HH.?",
            options=[
                "A) Como una herramienta estática y administrativa", 
                "B) Como un proceso dinámico sujeto a revisión continua", 
                "C) Como un método exclusivamente financiero"
            ],
            index=None
        )

        q5 = st.radio(
            "5. ¿Qué aportó Frederick Taylor al desarrollo del ADP?",
            options=[
                "A) La integración de factores emocionales en el trabajo", 
                "B) La idea de descomponer el trabajo en tareas simples y medibles", 
                "C) La creación de los sindicatos modernos"
            ],
            index=None
        )

        q6 = st.radio(
            "6. ¿Qué influencia tuvieron los periodos de guerra en la evolución del ADP?",
            options=[
                "A) Reducir la importancia de la organización del trabajo", 
                "B) Desarrollar métodos más sistemáticos de selección y asignación de puestos", 
                "C) Eliminar la necesidad de analizar los puestos"
            ],
            index=None
        )

        submitted = st.form_submit_button("Comprobar Respuestas")

    if submitted:
        st.subheader("Resultados")
        
        if q1 and q1.startswith("A"): st.success("Pregunta 1: ¡Correcto!") 
        else: st.error("Pregunta 1: Incorrecto. Las competencias son el conjunto de conocimientos, habilidades y actitudes (saber, saber hacer, saber ser).")
            
        if q2 and q2.startswith("B"): st.success("Pregunta 2: ¡Correcto!") 
        else: st.error("Pregunta 2: Incorrecto. Su objetivo principal es ofrecer una estructura objetiva para comprender y optimizar los puestos.")
            
        if q3 and q3.startswith("B"): st.success("Pregunta 3: ¡Correcto!") 
        else: st.error("Pregunta 3: Incorrecto. Históricamente, se usaba para clasificar tareas y asignar salarios.")
            
        if q4 and q4.startswith("B"): st.success("Pregunta 4: ¡Correcto!") 
        else: st.error("Pregunta 4: Incorrecto. Hoy en día es un proceso dinámico, estratégico y sujeto a revisión continua.")
            
        if q5 and q5.startswith("B"): st.success("Pregunta 5: ¡Correcto!") 
        else: st.error("Pregunta 5: Incorrecto. Taylor introdujo la organización científica mediante la descomposición en tareas medibles.")

        if q6 and q6.startswith("B"): st.success("Pregunta 6: ¡Correcto!") 
        else: st.error("Pregunta 6: Incorrecto. Obligaron a desarrollar métodos sistemáticos ante la escasez de recursos y la presión productiva.")

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
    st.write("Pon a prueba tus conocimientos sobre presupuestos, cotizaciones y costes salariales.")

    with st.form("quiz_economico_definitivo"):
        q1 = st.radio(
            "1. ¿Cuál es la función principal del presupuesto de personal más allá de calcular la necesidad neta de trabajadores?",
            options=[
                "A) Garantizar que todos los trabajadores reciban el mismo salario bruto independientemente de su puesto.", 
                "B) Comprobar la viabilidad financiera y actuar como instrumento de seguimiento para detectar desviaciones.", 
                "C) Servir únicamente como un listado detallado de los gastos fijos mensuales."
            ],
            index=None
        )
        
        q2 = st.radio(
            "2. ¿Qué ocurre con conceptos como el plus de transporte o las dietas en relación con la Seguridad Social?",
            options=[
                "A) Están exentos de cotización sin importar la cantidad que se abone al trabajador.", 
                "B) No computan en la base de cotización siempre que no superen los límites legales establecidos.", 
                "C) Cotizan siempre igual que el salario base para generar más derechos de jubilación."
            ],
            index=None
        )

        q3 = st.radio(
            "3. ¿Cómo ayuda el uso de una hoja de cálculo (análisis de sensibilidad) en la planificación de personal?",
            options=[
                "A) Se utiliza para sustituir al responsable de Recursos Humanos en la toma de decisiones.", 
                "B) Garantiza que la Seguridad Social no modifique las cuotas mensuales.", 
                "C) Permite simular diferentes escenarios, como el ahorro al cambiar tipos de contrato."
            ],
            index=None
        )

        q4 = st.radio(
            "4. ¿Qué ventaja tiene imputar los costes de personal por 'centros de coste' en departamentos distintos?",
            options=[
                "A) Permite delegar la responsabilidad del gasto y el control de horas extras en los mandos intermedios.", 
                "B) Elimina la necesidad de pagar cotizaciones a la Seguridad Social en el área comercial.", 
                "C) Hace que el coste hora sea exactamente el mismo para todos los departamentos."
            ],
            index=None
        )

        q5 = st.radio(
            "5. Al calcular el 'coste hora' de un trabajador para la empresa, ¿qué dos grandes bloques de gasto se deben sumar?",
            options=[
                "A) El salario neto del trabajador y los gastos de publicidad de la empresa.", 
                "B) El salario bruto percibido por el trabajador más las cotizaciones a cargo de la empresa.", 
                "C) El salario del trabajador y el alquiler de las oficinas."
            ],
            index=None
        )

        q6 = st.radio(
            "6. ¿Cómo influye el tipo de contrato en el coste de la cotización por desempleo para la empresa?",
            options=[
                "A) No influye en absoluto, ya que todos los trabajadores cotizan exactamente el mismo porcentaje por desempleo independientemente de su contrato.", 
                "B) Un contrato indefinido tiene un porcentaje de cotización por desempleo menor que un contrato temporal a tiempo parcial o formalizado mediante ETT.", 
                "C) Los contratos temporales y de Empresas de Trabajo Temporal (ETT) están totalmente exentos de cotizar por este concepto para fomentar el empleo."
            ],
            index=None
        )

        submitted = st.form_submit_button("Comprobar Respuestas")

    if submitted:
        st.subheader("Resultados")
        
        if q1 and q1.startswith("B"): st.success("Pregunta 1: ¡Correcto!") 
        else: st.error("Pregunta 1: Incorrecto. Su función es comprobar la viabilidad financiera y hacer seguimiento.")
            
        if q2 and q2.startswith("B"): st.success("Pregunta 2: ¡Correcto!") 
        else: st.error("Pregunta 2: Incorrecto. No computan en la base de cotización siempre que estén dentro del límite legal.")
            
        if q3 and q3.startswith("C"): st.success("Pregunta 3: ¡Correcto!") 
        else: st.error("Pregunta 3: Incorrecto. Permite hacer simulaciones (qué pasaría si...) para evaluar distintos escenarios económicos.")
            
        if q4 and q4.startswith("A"): st.success("Pregunta 4: ¡Correcto!") 
        else: st.error("Pregunta 4: Incorrecto. Imputarlo por centros de coste permite delegar la responsabilidad del gasto en cada mando intermedio.")
            
        if q5 and q5.startswith("B"): st.success("Pregunta 5: ¡Correcto!") 
        else: st.error("Pregunta 5: Incorrecto. Se suma el salario bruto y todas las cotizaciones a la Seguridad Social a cargo de la empresa.")

        if q6 and q6.startswith("B"): st.success("Pregunta 6: ¡Correcto!") 
        else: st.error("Pregunta 6: Incorrecto. Un contrato indefinido (tipo general) cotiza menos por desempleo que uno temporal o de ETT.")

elif seccion == "4. Técnicas de Recogida":
    st.title("4. Técnicas de Recogida de Información")

    st.write("Para analizar y describir un puesto de trabajo (ADP), existen múltiples métodos que van desde cuestionarios abiertos hasta la observación minuciosa. En la práctica empresarial, estas técnicas se agrupan en tres grandes bloques, además de un enfoque integrador.")

    st.header("4.1. Observación Directa")
    st.write("Consiste en que el analista observa y registra las conductas del trabajador durante la ejecución de sus tareas, sin intervenir (observación no participante).")
    st.markdown("* **Ejemplo:** Observar a un pintor de carrocería lijando y preparando un vehículo, anotando sus movimientos físicos y tiempos.")
    st.markdown("* **Ventajas:** Máxima objetividad (datos empíricos comprobables in situ) y profundidad cualitativa sobre el entorno físico.")
    st.markdown("* **Inconvenientes:** El \"Efecto Hawthorne\" (el trabajador altera su conducta al sentirse observado), la imposibilidad de registrar procesos mentales o toma de decisiones, y el alto coste en tiempo presencial.")

    st.header("4.2. Métodos de Interacción")
    st.write("Se basan en la comunicación verbal para indagar en aquello que no se ve a simple vista.")
    
    with st.expander("1. Entrevista Individual"):
        st.write("Se conversa directamente con el ocupante del puesto. Permite un trato personalizado y descubrir funciones no evidentes. Sin embargo, el trabajador puede sesgar la información (inflando sus tareas por ego, o minimizándolas por miedo a que le den más trabajo).")
    
    with st.expander("2. Entrevista de Incidentes Críticos"):
        st.write("Se pide al trabajador que describa situaciones extremas del pasado (grandes éxitos o fracasos). Es la herramienta más potente para identificar *competencias clave* (ej. tolerancia a la frustración), aunque ofrece una visión parcial y deja fuera la rutina diaria.")
    
    with st.expander("3. Reunión de Paneles de Expertos"):
        st.write("Se reúne al trabajador, su supervisor y el analista (que actúa de moderador) para consensuar la información. Genera gran sinergia y es eficiente, pero pueden surgir \"dinámicas de poder\" que inhiban al empleado de hablar libremente ante su jefe.")

    st.header("4.3. Métodos de Registro")
    st.write("La responsabilidad de recopilar los datos recae en el propio trabajador o en su supervisor.")
    
    with st.expander("1. Cuestionarios y Listas de Chequeo"):
        st.write("Documentos estructurados (escalas, preguntas cerradas). Son rápidos, económicos y permiten el análisis estadístico. Su problema principal: si son genéricos no se adaptan a la jerga de la empresa, y si son a medida, requieren conocimientos avanzados de psicometría para diseñarlos bien.")
    
    with st.expander("2. Diario de Trabajo"):
        st.write("El trabajador anota sus actividades en intervalos de tiempo preestablecidos. Muy útil para cuantificar tiempos y detectar cuellos de botella. Sus grandes retos son la falta de homogeneidad (unos escriben mucho, otros poco), la posible falta de sinceridad y la fricción que genera interrumpir el trabajo físico para escribir.")

    st.header("4.4. La necesidad de un Enfoque Mixto: La Triangulación")
    st.success("""
**Triangulación metodológica:**
Ninguna técnica es perfecta por sí sola. La observación capta lo físico pero ignora lo mental; la entrevista profundiza pero tiene sesgos; los cuestionarios son masivos pero pierden detalle. 

Por ello, la práctica moderna exige combinar dos o más herramientas (ej. cuestionario previo + observación in situ + entrevista final de validación) para que las fortalezas de una compensen las debilidades de la otra, garantizando un ADP riguroso.
""")

    st.markdown("---")
    st.header("Autoevaluación")
    st.write("Pon a prueba tus conocimientos sobre los métodos para obtener información de los puestos.")

    with st.form("quiz_tecnicas_definitivo"):
        q1 = st.radio(
            "1. ¿Cuál es uno de los principales retos o inconvenientes de la técnica de observación directa no participante?",
            options=[
                "A) No permite obtener datos objetivos sobre los movimientos físicos y tiempos empleados por el trabajador.", 
                "B) No permite registrar ni analizar procesos mentales, emocionales o de toma de decisiones complejas.", 
                "C) Su rapidez y economía hacen que se pierda profundidad en el análisis de las tareas."
            ],
            index=None
        )
        
        q2 = st.radio(
            "2. ¿En qué se centra principalmente la Entrevista de Incidentes Críticos?",
            options=[
                "A) En recopilar de forma ágil datos estadísticos y cerrados sobre el uso de herramientas en la jornada laboral.", 
                "B) En identificar las competencias clave del puesto mediante la descripción de situaciones extremas concretas y pasadas.", 
                "C) En registrar pormenorizadamente las actividades rutinarias y tareas monótonas que el trabajador realiza cada día."
            ],
            index=None
        )

        q3 = st.radio(
            "3. ¿Qué inconveniente puede surgir en una Reunión de Paneles de Expertos si el moderador no es lo suficientemente hábil?",
            options=[
                "A) Pueden surgir dinámicas de poder que cohíban a los empleados a la hora de hablar abiertamente delante de sus supervisores.", 
                "B) El trabajador puede inventarse actividades y exagerar los tiempos empleados para justificar su salario.", 
                "C) La información recopilada estará fuertemente sesgada por la falta de adaptación del vocabulario técnico."
            ],
            index=None
        )

        q4 = st.radio(
            "4. ¿Cuál es una de las principales fortalezas del uso de cuestionarios y listas de chequeo para la recogida de información?",
            options=[
                "A) Su rapidez y economía, ya que son de fácil administración y permiten llegar a muchos trabajadores a la vez.", 
                "B) Fomentan la observación in situ y el análisis cualitativo del entorno físico del trabajador.", 
                "C) Permiten registrar y analizar procesos mentales, emocionales y de toma de decisiones complejas."
            ],
            index=None
        )

        q5 = st.radio(
            "5. ¿Qué implica aplicar un enfoque mixto o de triangulación metodológica en el Análisis y Descripción de Puestos?",
            options=[
                "A) Dividir el proceso de análisis en tres fases secuenciales supervisadas por tres analistas externos.", 
                "B) Combinar dos o más herramientas de recogida de datos para que las fortalezas de una compensen las debilidades de la otra.", 
                "C) Seleccionar siempre a tres trabajadores clave de un mismo departamento para realizar el análisis simultáneamente."
            ],
            index=None
        )

        q6 = st.radio(
            "6. ¿Cuál es uno de los principales retos o inconvenientes operativos al utilizar la técnica del 'Diario de Trabajo' para recopilar información?",
            options=[
                "A) Requiere una elevada inversión económica y de tiempo al obligar al analista a estar presente toda la jornada.", 
                "B) Genera fricción e incomodidad, ya que obliga al trabajador a interrumpir constantemente su labor física para registrar sus actividades.", 
                "C) Solo permite obtener información sobre situaciones excepcionales o críticas, dejando fuera las rutinas diarias."
            ],
            index=None
        )

        submitted = st.form_submit_button("Comprobar Respuestas")

    if submitted:
        st.subheader("Resultados")
        
        if q1 and q1.startswith("B"): st.success("Pregunta 1: ¡Correcto!") 
        else: st.error("Pregunta 1: Incorrecto. Su mayor límite es cognitivo, no permite evaluar procesos mentales o toma de decisiones.")
            
        if q2 and q2.startswith("B"): st.success("Pregunta 2: ¡Correcto!") 
        else: st.error("Pregunta 2: Incorrecto. Se centra en comportamientos pasados ante situaciones extremas para detectar competencias.")
            
        if q3 and q3.startswith("A"): st.success("Pregunta 3: ¡Correcto!") 
        else: st.error("Pregunta 3: Incorrecto. El principal riesgo es que la jerarquía intimide al trabajador.")
            
        if q4 and q4.startswith("A"): st.success("Pregunta 4: ¡Correcto!") 
        else: st.error("Pregunta 4: Incorrecto. Destacan por ser económicos y llegar masivamente a la plantilla rápidamente.")
            
        if q5 and q5.startswith("B"): st.success("Pregunta 5: ¡Correcto!") 
        else: st.error("Pregunta 5: Incorrecto. Consiste en combinar métodos (ej. cuestionario + entrevista) para un resultado integral.")

        if q6 and q6.startswith("B"): st.success("Pregunta 6: ¡Correcto!") 
        else: st.error("Pregunta 6: Incorrecto. Es un método incómodo en puestos manuales o de cadena de montaje.")

elif seccion == "5. Metodología y Estrategia":
    st.title("5. Metodología y Estrategia del ADP")

    st.write("El Análisis y Descripción de Puestos no es un fin en sí mismo, sino la \"pieza maestra\" que alimenta todos los procesos estratégicos de la organización.")

    st.header("5.1. Importancia Estratégica")
    st.write("El ADP resuelve la desorientación interna al delimitar tareas y niveles de autoridad, impactando en:")
    st.markdown("* **Vínculo con la Selección:** Define el \"perfil ideal\" o profesiograma, permitiendo un reclutamiento basado en exigencias reales y no en intuiciones.")
    st.markdown("* **Vínculo con la Formación:** Al comparar el perfil real del trabajador con lo que el puesto exige, se detectan \"lagunas\" de conocimiento para invertir en formación de forma rentable.")
    st.markdown("* **Determinación de Responsabilidades:** Reduce la incertidumbre y evita la \"ambigüedad de rol\", una de las mayores causas de conflicto interno.")

    st.header("5.2. Salud Laboral y Prevención de Riesgos")
    st.write("El ADP es el instrumento técnico básico para las cuatro especialidades preventivas:")
    st.markdown("1. **Seguridad en el Trabajo:** Identifica riesgos en máquinas y espacios.")
    st.markdown("2. **Higiene Ocupacional:** Controla la exposición a agentes físicos, químicos o biológicos.")
    st.markdown("3. **Ergonomía y Psicosociología:** Detecta riesgos por carga física, posturas, fatiga y estrés (aquí el ADP es crítico).")
    st.markdown("4. **Medicina del Trabajo:** Proporciona datos para la vigilancia de la salud específica.")

    st.success("**Principio Fundamental:** La gestión debe \"adaptar el trabajo a la persona\", especialmente en el diseño de puestos y elección de equipos.")

    st.header("5.3. Análisis Operativo: Las 5 Cuestiones Básicas")
    st.write("Un análisis de alta calidad debe responder con rigor a:")
    st.markdown("1. **¿Qué hace?** (Tareas valoradas por importancia y tiempo).")
    st.markdown("2. **¿Cómo lo hace?** (Métodos, instrucciones y riesgos asumidos).")
    st.markdown("3. **¿Con qué lo hace?** (Máquinas, herramientas y materiales).")
    st.markdown("4. **¿Por qué lo hace?** (Misión y finalidad dentro de la cadena de valor).")
    st.markdown("5. **¿Quién lo hace?** (Requisitos humanos: aptitudes, formación y capacidades mentales).")

    st.header("5.4. Participantes y Selección de Puestos")
    st.markdown("* **Participantes:** El Analista (experto técnico), el Titular (fuente primaria), el Responsable Jerárquico (validador) y RR.HH. (responsable global).")
    st.markdown("* **Criterio de Selección:** En estructuras complejas se usa la **Representatividad**, analizando puestos \"tipo\".")
    st.markdown("* **Métodos de Identificación:** Para saber qué puestos son únicos se puede: consultar registros de RR.HH., validar con jefes de área, preguntar a empleados o realizar una investigación exhaustiva (el método más científico y costoso).")

    st.markdown("---")
    st.header("Autoevaluación")
    st.write("Pon a prueba tus conocimientos sobre la metodología, estrategia y aplicación práctica del ADP.")

    with st.form("quiz_metodologia_definitivo"):
        q1 = st.radio(
            "1. ¿De qué manera el Análisis de Puestos ayuda a la planificación de la formación?",
            options=[
                "A) Determinando las carencias de conocimientos al comparar el perfil real con el ideal", 
                "B) Reduciendo los costes salariales de los empleados recién contratados", 
                "C) Eliminando la necesidad de realizar entrevistas de selección"
            ],
            index=None
        )
        
        q2 = st.radio(
            "2. Según los principios de prevención en salud laboral, ¿cuál es un objetivo fundamental del ADP?",
            options=[
                "A) Que el trabajador aumente su ritmo de producción de forma indefinida", 
                "B) Adaptar el trabajo a la persona para evitar daños a la salud", 
                "C) Sustituir obligatoriamente a los trabajadores por maquinaria automática"
            ],
            index=None
        )

        q3 = st.radio(
            "3. Dentro del análisis operativo, ¿qué se busca definir con la pregunta '¿Por qué lo hace?'?",
            options=[
                "A) Las herramientas informáticas y máquinas necesarias para el puesto", 
                "B) Los requisitos de formación y las aptitudes físicas exigidas", 
                "C) La finalidad y el objetivo que persigue la tarea para la organización"
            ],
            index=None
        )

        q4 = st.radio(
            "4. ¿En qué consiste el 'Criterio de Representatividad' al seleccionar puestos para un estudio?",
            options=[
                "A) En analizar absolutamente todos los puestos de la plantilla de forma individual", 
                "B) En elegir un puesto 'tipo' por cada línea de producto o división funcional", 
                "C) En seleccionar únicamente a los trabajadores que tienen mayor antigüedad"
            ],
            index=None
        )

        q5 = st.radio(
            "5. ¿Cuál es una 'Regla de Oro' indispensable al redactar una descripción de puesto?",
            options=[
                "A) Basarse exclusivamente en hechos reales y no en opiniones subjetivas", 
                "B) Utilizar adjetivos como 'aburrido' o 'interesante' para describir la tarea", 
                "C) Incluir detalles anecdóticos e 'historietas' para que el texto sea más largo"
            ],
            index=None
        )

        q6 = st.radio(
            "6. Durante la planificación del proyecto de ADP, ¿por qué es vital la comunicación a la plantilla?",
            options=[
                "A) Para que los trabajadores puedan elegir libremente su propio horario de análisis", 
                "B) Para evitar rumores y motivar la colaboración de los empleados en el proceso", 
                "C) Para informar sobre cambios inmediatos en el sistema de retribución variable"
            ],
            index=None
        )

        q7 = st.radio(
            "7. En el proceso de elaboración del Análisis y Descripción de Puestos (ADP), ¿cuál es la función principal del 'Responsable Jerárquico'?",
            options=[
                "A) Actuar como el experto técnico que aporta la metodología rigurosa para obtener los datos", 
                "B) Validar que lo expresado por el trabajador y el analista coincide con la realidad operativa del departamento", 
                "C) Asumir la responsabilidad global del proyecto y decidir su presupuesto y oportunidad estratégica"
            ],
            index=None
        )

        submitted = st.form_submit_button("Comprobar Respuestas")

    if submitted:
        st.subheader("Resultados")
        
        if q1 and q1.startswith("A"): st.success("Pregunta 1: ¡Correcto!") 
        else: st.error("Pregunta 1: Incorrecto. Permite detectar 'lagunas' comparando el perfil ideal del ADP con el perfil real del empleado.")
            
        if q2 and q2.startswith("B"): st.success("Pregunta 2: ¡Correcto!") 
        else: st.error("Pregunta 2: Incorrecto. El principio clave en salud laboral es adaptar el trabajo (entorno, equipos) a la persona.")
            
        if q3 and q3.startswith("C"): st.success("Pregunta 3: ¡Correcto!") 
        else: st.error("Pregunta 3: Incorrecto. Responde al propósito o misión final de la tarea.")
            
        if q4 and q4.startswith("B"): st.success("Pregunta 4: ¡Correcto!") 
        else: st.error("Pregunta 4: Incorrecto. Consiste en elegir un puesto 'tipo' representativo y evitar analizarlos todos uno por uno.")
            
        if q5 and q5.startswith("A"): st.success("Pregunta 5: ¡Correcto!") 
        else: st.error("Pregunta 5: Incorrecto. La descripción debe fijarse en hechos comprobables y lenguaje objetivo y neutral.")

        if q6 and q6.startswith("B"): st.success("Pregunta 6: ¡Correcto!") 
        else: st.error("Pregunta 6: Incorrecto. Es vital para evitar rumores falsos y buscar la colaboración del personal.")

        if q7 and q7.startswith("B"): st.success("Pregunta 7: ¡Correcto!") 
        else: st.error("Pregunta 7: Incorrecto. Su principal función es validar que lo expresado por el trabajador coincide con la realidad operativa real.")
