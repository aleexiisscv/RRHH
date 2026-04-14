import streamlit as st
import graphviz

# Configuración inicial de la página
st.set_page_config(page_title="Análisis y Descripción de Puestos", layout="wide")

# Inicialización de la variable de estado para manejar la navegación
if 'step' not in st.session_state:
    st.session_state.step = 1

def next_step():
    """Avanza al siguiente paso."""
    if st.session_state.step < 3:
        st.session_state.step += 1

def prev_step():
    """Retrocede al paso anterior."""
    if st.session_state.step > 1:
        st.session_state.step -= 1

# Título y navegación superior
st.sidebar.title("Navegación del ADP")
st.sidebar.markdown(f"**Paso actual: {st.session_state.step} de 3**")

# Botones de navegación en la barra lateral
col1, col2 = st.sidebar.columns(2)
with col1:
    st.button("Anterior", on_click=prev_step, disabled=st.session_state.step == 1, use_container_width=True)
with col2:
    st.button("Siguiente", on_click=next_step, disabled=st.session_state.step == 3, use_container_width=True)

st.sidebar.divider()

# ----- PASO 1 -----
if st.session_state.step == 1:
    st.title("Paso 1: El Laberinto Teórico")
    st.markdown("""
    En el Análisis y Descripción de Puestos (ADP) existen diferentes técnicas formales, pero usarlas de forma aislada deja **puntos ciegos**:
    
    *   **La observación** capta lo físico pero ignora los procesos mentales del trabajador.
    *   **La entrevista** profundiza en los detalles, pero puede estar sujeta a sesgos cognitivos o percepciones equivocadas.
    *   **Los cuestionarios** abarcan mucha información de forma rápida, pero pierden el detalle cualitativo.
    """)
    
    # Generación de gráfico Graphviz de Nodos Aislados
    graph = graphviz.Digraph(comment='El Laberinto Teórico')
    graph.attr(rankdir='LR', size='8,5')
    
    # Nodos sin conexiones
    graph.node('obs', 'Observación\nDirecta', color='dodgerblue', style='filled', fontcolor='white', shape='circle')
    graph.node('ent', 'Métodos de Interacción\n(Entrevistas)', color='crimson', style='filled', fontcolor='white', shape='circle')
    graph.node('cue', 'Métodos de Registro\n(Cuestionarios)', color='forestgreen', style='filled', fontcolor='white', shape='circle')
    
    st.graphviz_chart(graph)

# ----- PASO 2 -----
elif st.session_state.step == 2:
    st.title("Paso 2: La Triangulación Metodológica")
    st.markdown("""
    La verdadera solución en el entorno de recursos humanos es un **enfoque mixto**. 
    
    La **triangulación metdológica** es la acción de combinar herramientas para que las fortalezas de unas compensen las debilidades de las otras.
    """)
    
    # Generación de gráfico Graphviz de Convergencia
    graph = graphviz.Digraph(comment='Triangulación')
    graph.attr(rankdir='LR') # De izquierda a derecha
    
    # Nodos originales
    graph.node('obs', 'Observación\nDirecta', color='dodgerblue', style='filled', fontcolor='white', shape='circle')
    graph.node('ent', 'Métodos de Interacción\n(Entrevistas)', color='crimson', style='filled', fontcolor='white', shape='circle')
    graph.node('cue', 'Métodos de Registro\n(Cuestionarios)', color='forestgreen', style='filled', fontcolor='white', shape='circle')
    
    # Nodo central convergente
    graph.node('tri', 'Triangulación\nMetodológica', color='indigo', style='filled, bold', fontcolor='white', shape='box', fontsize='16')
    
    # Aristas (flechas) hacia el centro
    graph.edge('obs', 'tri')
    graph.edge('ent', 'tri')
    graph.edge('cue', 'tri')
    
    st.graphviz_chart(graph)

# ----- PASO 3 -----
elif st.session_state.step == 3:
    st.title("Paso 3: Aplicación al Caso Práctico (El Pintor)")
    st.markdown("""
    Finalmente, aplicamos la triangulación al análisis concreto del puesto de un **pintor de carrocería**. El análisis se divide en 3 fases secuenciales:
    
    1.  **Amplitud**: Uso de cuestionarios para definir los EPIs básicos requeridos y mapear competencias superficiales.
    2.  **Realidad Física**: Uso de la observación directa para inspeccionar el entorno físico en el que el pintor opera y tomar tiempos de ejecución.
    3.  **Profundidad**: Aplicación de la Entrevista de Incidentes Críticos para evaluar directamente cómo el operario resuelve problemas complejos y situaciones imprevistas.
    """)
    
    # Generación de gráfico Graphviz de Flujo Secuencial Lineal
    graph = graphviz.Digraph(comment='El Pintor')
    graph.attr(rankdir='LR', size='10,4')
    
    graph.node('F1', 'Fase 1: Cuestionarios\n(Amplitud)', shape='note', style='filled', color='lightblue', fontcolor='black')
    graph.node('F2', 'Fase 2: Observación Directa\n(Entorno Físico)', shape='note', style='filled', color='lightgreen', fontcolor='black')
    graph.node('F3', 'Fase 3: Entrevista de\nIncidentes Críticos\n(Profundidad)', shape='note', style='filled', color='lightcoral', fontcolor='black')
    
    graph.edge('F1', 'F2', label=' Siguiente Paso')
    graph.edge('F2', 'F3', label=' Siguiente Paso')
    
    st.graphviz_chart(graph)
