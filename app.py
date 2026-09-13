import streamlit as st
import pandas as pd 
import plotly.express as px

# rozkład strony internetowej

st.set_page_config(page_title= "Analiza Czasu Produkcji", layout="wide")
st.title("Panel Analityczny: Czasu Produkcji")

@st.cache_data
def load_data(file):
    df = pd.read_csv(file, sep=None, engine='python')
    df['Zmiana w toku'] = pd.to_datetime(df['Zmiana na W Toku'], format="%d.%m.%Y %H:%M", errors='coerce')
    df['Czas (Godziny)'] = df['Roznica czasow(Minuty)']/60

    return df 

uploaded_file = st.sidebar.file_uploader(
    "Wgraj plik CSV (tylko)", 
    type=["csv"]
)

#bramka kontrolna czy plik CSV został wgrany 

if uploaded_file is not None:
    
    df = load_data(uploaded_file)

    #zarządzanie pamięcia 

    # panel boczny aplikacji
    st.sidebar.header("Filtry")
    wybranie_pracownicy = st.sidebar.multiselect(
        "Wybierz pracownika:",
        options=df['Przypisany Do'].dropna().unique(),
        default=df['Przypisany Do'].dropna().unique()
    )

    #filtracja danych na podstawie wybranych pracowników
    filtered_df = df[df['Przypisany Do'].isin(wybranie_pracownicy)]

    st.markdown("### Podsumowanie(KPI)")

    # OBLICZENIA NA PRZEFILTROWANYM DATAFRAME 
    total_godziny = filtered_df["Czas (Godziny)"].sum()
    liczba_zadan = len(filtered_df)
    sredni_czas = filtered_df["Czas (Godziny)"].mean() if liczba_zadan > 0 else 0 


    # tworzenie trzech kolum osok siebie w celu wyświetlenia KPI

    col1, col2, col3 = st.columns(3)

    col1.metric("Całkowity czas pracy (Godziny)", f"{total_godziny:.2f} h")
    col2.metric("Liczba zadań", f"{liczba_zadan}")
    col3.metric("Średni czas zadania", f"{sredni_czas:.2f} h")

    st.markdown("---")  # separator 
    st.subheader("Wizualizacja danych")

    # tworzymy dwie kolumny obok sieie do wyświtetlania dwóch wykresów 
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.write("**Czas Pracy Pracowników**")
        # Najpierw grupujemy dane i sumujemy czas dla danego pracownika 
        df_pracownicy = filtered_df.groupby("Przypisany Do")["Czas (Godziny)"].sum().reset_index()

        # Tworzymy wykres słupkowy z użyciem plotly express
        fig_pracownicy = px.bar( 
            df_pracownicy, 
            x="Przypisany Do",
            y="Czas (Godziny)",
            color="Przypisany Do",
            title="Suma Godzin wg Pracownika"
        )
        st.plotly_chart(fig_pracownicy, use_container_width=True)
    with col_chart2:
        st.write("**Czas Poświęcony na Podespoły**")
        # grupujemy dane i sumujemy czas dla danego podzespołu
        df_podzespoły = filtered_df.groupby("Podzespol")["Czas (Godziny)"].sum().reset_index()

        # generujemy wykres słupkowy z użyciem plotly express
        fig_podzespoły = px.bar(
            df_podzespoły,
            x="Podzespol",
            y="Czas (Godziny)",
            title="Suma godzin wg Pozdzespołu"
        )
        # pokazujemy wykres na stronie
        st.plotly_chart(fig_podzespoły, use_container_width=True)

    st.markdown("---") 

    # podgląd teabeli na środku ekranu 

    st.subheader("Podgląd przefiltrwanych danych")
    st.dataframe(filtered_df)

else: 
    st.warning("Proszę załadować plik CSV aby kontynuować analizę danych.")
    st.stop()