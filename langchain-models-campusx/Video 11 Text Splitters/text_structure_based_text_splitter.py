from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = """ 
Diljit Dosanjh (born 6 January 1984) is an Indian singer, actor and film producer who works in Punjabi and Hindi cinema.[2][3] Dosanjh entered the Social 50 chart by Billboard in 2020.[4] He has been featured in various music charts, including the Canadian Albums Chart, the UK Asian chart by Official Charts Company and the New Zealand Hot Singles. His films, including Jatt & Juliet 2, Sajjan Singh Rangroot, Honsla Rakh and Jatt & Juliet 3 are among the highest grossing Punjabi films in history.[5]

Hailing from Dosanjh Kalan, Jalandhar district, Dosanjh began his career in 2002 and gained recognition in Punjabi music with his albums Smile (2005) and Chocolate (2008), followed by the blockbuster album; The Next Level (2009) with Yo Yo Honey Singh. He had a cameo in the Punjabi movie Mel Karade Rabba in 2010 and began to pursue acting, debuting as a leading actor in the Punjabi movie The Lion of Punjab in 2011.[3]

He made his Bollywood debut in 2016 with the crime thriller Udta Punjab, for which he earned the Filmfare Award for Best Male Debut, in addition to a nomination for the Filmfare Award for Best Supporting Actor. This was followed by Good Newwz (2019), for which he received his second nomination for the Filmfare Award for Best Supporting Actor. As of 2020, he has won the PTC Award for Best Actor five times. He has also appeared as a judge in three seasons of the reality show Rising Star.[6]

In 2020, Dosanjh charted on the Social 50 chart by Billboard with the release of his 11th album, G.O.A.T..[4]"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

result = splitter.split_text(text)

print(result)