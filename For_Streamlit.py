# %%
import pandas as pd

# %%
https://drive.google.com/file/d/1XsLa1irI_y60hiOi0NGk-8gnCCSQN2N3/view?usp=sharing

#Spotify 1 data 
#From csv file on google drive with shareable link set to anyone can view 

# %%
a_url='https://drive.google.com/file/d/1XsLa1irI_y60hiOi0NGk-8gnCCSQN2N3/view?usp=sharing'
path='https://drive.google.com/uc?id=' + a_url.split('/')[-2]
Spotify_1_csv_data = pd.read_csv(path)

# %%
print (Spotify_1_csv_data)

# %%
https://docs.google.com/spreadsheets/d/1CeVNC7YBvef2w8pT_0rErfuUxs5iuC5yoYoTSj9evfE/edit?usp=drive_link

#Spotify 1 data
#From google sheets on google drive with shareable link set to anyone can view 

# %%
sheet_name = 'Spotify_1_data' # replace with your own sheet name
sheet_id = '1CeVNC7YBvef2w8pT_0rErfuUxs5iuC5yoYoTSj9evfE' # replace with your sheet's ID

# %%
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# %%
data = pd.read_csv(url)
print(data)

# %%
https://drive.google.com/file/d/1XoBIxdGZrnTmmzyaKNS4-I692vtK2q-X/view?usp=sharing

#Spotify 2 data 

# %%
Spotify_2_url='https://drive.google.com/file/d/1XoBIxdGZrnTmmzyaKNS4-I692vtK2q-X/view?usp=sharing'
Spotify_2_path='https://drive.google.com/uc?id=' + Spotify_2_url.split('/')[-2]
Spotify_2_csv_data = pd.read_csv(Spotify_2_path)

# %%
print (Spotify_2_csv_data)

# %%
https://drive.google.com/file/d/1XnjLLT-0W0xYmGgMHWRIwwaqA2WS1Re2/view?usp=sharing

#Spotify 3 Data

# %%
Spotify_3_url='https://drive.google.com/file/d/1XnjLLT-0W0xYmGgMHWRIwwaqA2WS1Re2/view?usp=sharing'
Spotify_3_path='https://drive.google.com/uc?id=' + Spotify_3_url.split('/')[-2]
Spotify_3_csv_data = pd.read_csv(Spotify_3_path)

# %%
print (Spotify_3_csv_data)

# %%
https://drive.google.com/file/d/1XlvC8S3z7a698BzXQ4XoPdIAEzMzk_-9/view?usp=sharing

#Spotify 4 Data

# %%
Spotify_4_url='https://drive.google.com/file/d/1XlvC8S3z7a698BzXQ4XoPdIAEzMzk_-9/view?usp=sharing'
Spotify_4_path='https://drive.google.com/uc?id=' + Spotify_4_url.split('/')[-2]
Spotify_4_csv_data = pd.read_csv(Spotify_4_path)

# %%
print(Spotify_4_csv_data)

# %%
Merging_Spotify_data = Spotify_1_csv_data[['track_name', 'artist.s._name', 'streams']]

print(Merging_Spotify_data)

# %%
More_merging = pd.concat ([Merging_Spotify_data, Spotify_2_csv_data])

print(More_merging)

# %%
Extraction = More_merging[['track_name', 'artist.s._name', 'streams']]

print(Extraction)

# %%
Even_more_merging = pd.concat ([Extraction, Spotify_3_csv_data])

print (Even_more_merging)

# %%
Even_more_extraction = Even_more_merging[['track_name', 'artist.s._name', 'streams']]

print(Even_more_extraction)

# %%
The_final_merge = pd.concat ([Even_more_extraction, Spotify_4_csv_data])

print(The_final_merge)

# %%
The_final_extraction = The_final_merge[['track_name', 'artist.s._name', 'streams']]

print(The_final_extraction)

# %%
pip install sqlitecloud

# %%
import io

# %%
import sqlitecloud

# %%
conn = sqlitecloud.connect("sqlitecloud://cutggajrnk.sqlite.cloud:8860/Spotifystuff?apikey=P6MDqNpiO0ppuGnybsssYxbEqwi0npW9xb5brL4aKkE")


# %%
The_final_extraction.to_sql("Spotifystuff", conn, index=False)

# %%
Double_checking=pd.read_sql("SELECT * FROM Spotifystuff", conn)

print(Double_checking)

# %%
pip install streamlit


# %%
import streamlit as st
 

# %%
st.bar_chart(data=Double_checking, x='track_name', y='streams', x_label='Name of track', y_label='Number of streams', color= None, horizontal=False, stack=False, width=False,
height=False, use_container_width=True)

# %%
print(st.bar_chart)


