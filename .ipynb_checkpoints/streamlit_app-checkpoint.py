{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ebd5b5c0-fcc5-4a9e-bf23-21946406216b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-05-01 19:52:01.135 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.137 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.137 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.138 No runtime found, using MemoryCacheStorageManager\n",
      "2025-05-01 19:52:01.148 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.158 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.159 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.159 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.160 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.160 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.160 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.161 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.161 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.163 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.164 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.164 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.167 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.168 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.190 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.190 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.190 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.191 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.193 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.193 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.203 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.401 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.401 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.402 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.402 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.402 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.402 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.402 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-05-01 19:52:01.402 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import folium\n",
    "from folium.plugins import HeatMap\n",
    "from streamlit_folium import st_folium\n",
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "# Sayfa ayarları\n",
    "st.set_page_config(page_title=\"Marmara Deprem Analizi\", layout=\"wide\")\n",
    "\n",
    "st.title(\"🌍 Marmara Deprem Analizi ve Görselleştirme (2000–2025)\")\n",
    "\n",
    "# Veri Yükle\n",
    "@st.cache_data\n",
    "def load_data():\n",
    "    df = pd.read_csv(\"marmara_faults_earthquakes_2000_2025.csv\")\n",
    "    df['Date'] = pd.to_datetime(df['Date'])\n",
    "    df = df[(df['Latitude'] > 39) & (df['Latitude'] < 42) &\n",
    "            (df['Longitude'] > 26) & (df['Longitude'] < 31)].copy()\n",
    "    df['Year'] = df['Date'].dt.year\n",
    "    return df\n",
    "\n",
    "df = load_data()\n",
    "\n",
    "# Sidebar filtreler\n",
    "st.sidebar.header(\"Filtreler\")\n",
    "years = sorted(df['Year'].unique())\n",
    "selected_year = st.sidebar.slider(\"Yıl\", int(min(years)), int(max(years)), 2023)\n",
    "min_mag, max_mag = st.sidebar.slider(\"Büyüklük Aralığı (ML)\", 2.0, 7.5, (2.0, 6.0))\n",
    "\n",
    "# Filtreli veri\n",
    "filtered_df = df[(df['Year'] == selected_year) &\n",
    "                 (df['Magnitude_ML'] >= min_mag) & (df['Magnitude_ML'] <= max_mag)]\n",
    "\n",
    "# Harita\n",
    "st.subheader(f\"{selected_year} Yılı Deprem Yoğunluk Haritası\")\n",
    "map_center = [40.8, 29.0]\n",
    "m = folium.Map(location=map_center, zoom_start=8)\n",
    "heat_data = [[row['Latitude'], row['Longitude'], row['Magnitude_ML']] \n",
    "             for index, row in filtered_df.iterrows()]\n",
    "HeatMap(heat_data, radius=10, max_zoom=13).add_to(m)\n",
    "st_folium(m, width=1000, height=500)\n",
    "\n",
    "# Zaman serisi - Yıllık deprem sayısı\n",
    "yearly_counts = df.groupby('Year').size().reset_index(name='Quake_Count')\n",
    "\n",
    "st.subheader(\"📈 Yıllık Deprem Sayısı ve Tahmini\")\n",
    "X = yearly_counts['Year'].values.reshape(-1, 1)\n",
    "y = yearly_counts['Quake_Count'].values\n",
    "model = LinearRegression()\n",
    "model.fit(X, y)\n",
    "future_years = np.array([[2026], [2027], [2028], [2029], [2030]])\n",
    "future_preds = model.predict(future_years)\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(10, 4))\n",
    "ax.scatter(X, y, color='blue', label='Gerçek Veriler')\n",
    "ax.plot(X, model.predict(X), color='orange', label='Model (Geçmiş)')\n",
    "ax.plot(future_years, future_preds, 'g--', label='Tahmin (2026–2030)')\n",
    "ax.set_xlabel(\"Yıl\")\n",
    "ax.set_ylabel(\"Deprem Sayısı\")\n",
    "ax.legend()\n",
    "ax.grid(True)\n",
    "st.pyplot(fig)\n",
    "\n",
    "# Tahminleri tablo halinde göster\n",
    "st.markdown(\"### 📅 2026–2030 Tahmini Deprem Sayıları\")\n",
    "pred_df = pd.DataFrame({\n",
    "    'İl': future_years.ravel(),\n",
    "    'Tahmini Deprem Sayısı': future_preds.astype(int)\n",
    "})\n",
    "st.dataframe(pred_df, use_container_width=True)\n",
    "\n",
    "st.markdown(\"---\")\n",
    "st.markdown(\"Bu uygulama, Marmara Bölgesi'ndeki depremlerin zamansal ve mekansal analizi için geliştirilmiştir. \")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ebcb9655-6d3b-4c7d-a537-ea98bd2557ef",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2482160671.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[6], line 1\u001b[0;36m\u001b[0m\n\u001b[0;31m    streamlit run streamlit_app.py\u001b[0m\n\u001b[0m              ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run streamlit_app.py\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f14c6f9c-9b7d-4899-bbce-aab42578388b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
