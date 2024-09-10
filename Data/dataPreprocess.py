import pandas as pd
import numpy as np


movies_df = pd.read_csv("VIP Files\TMDBmoviesData.csv")
# movies_df['title'] = movies_df['title'].str.replace(",", ".")
# movies_df['poster_path'] = movies_df['poster_path'].str.replace(",", "_")
movieID = np.arange(1, 1001)
movies_df.insert(0, 'movie_ID', movieID)
print(movies_df)
movies_df.to_csv("VIP Files\TMDBmoviesData.csv", index=False)


