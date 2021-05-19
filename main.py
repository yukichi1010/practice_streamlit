import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit入門')

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目':[1, 2, 3, 4], 
#     '2列目':[10, 20, 30, 40], 
# })

# dataframeならサイズなどの細かい内容を指定可能。
# tableではstatic(静的)なテーブルが使用可能。
# axisが0なら列, 行なら1。
# jsonを表示可能。
# 詳しいことはdocsのAPI referenceからDisplay dataを参照。
# st.write(df)
# st.dataframe(df, width=100, height=100)
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))
# --------------------------------------------------------------------------------------

# マジックコマンド。
# markdown方式で表示される。
# st.markdown()で表示することも可能。
# ほかにもLatexも表示可能。
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
# --------------------------------------------------------------------------------------

# チャートを記載。
# df = pd.DataFrame(
#     np.random.rand(20, 3), 
#     columns=['a', 'b', 'c']
# )

# 詳しいことはdocsのAPI referenceからDisplay chartを参照。
# 折れ線グラフで表示。
# st.line_chart(df)
# 折れ線の下の部分を塗りつぶしたもの。
# st.area_chart(df)
# 棒グラフで表示。
# st.bar_chart(df)
# --------------------------------------------------------------------------------------

# マップをプロット
# Display chartに詳しいことが書いてある。
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.635054, 139.356443], 
#     columns=['lat', 'lon']
# )
# st.map(df)
# --------------------------------------------------------------------------------------

# st.write('Display Image')

# img = Image.open('SPOILER_matikane.png')

# use_column_widthはその列幅を使用する。
# captionは画像のタイトル。
# Display mediaよりさらに詳しく。
# st.image(img, caption='matikane', use_column_width=True)

# if st.checkbox('Show Image'):
#     img = Image.open('SPOILER_matikane.png')
#     st.image(img, caption='matikane', use_column_width=True)
# --------------------------------------------------------------------------------------

# st.write('Interactive Widgets')
# インタラクティブなウィジェット
# optionやtextは動的に変化し、ユーザーが値を変更するたびに変数の値も変化する。
# Display interactive wigetsにさらに詳しく。
# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい。', 
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です。'

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition
# --------------------------------------------------------------------------------------
 
# レイアウトを整える。
# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition
# --------------------------------------------------------------------------------------

# 2カラムレイアウト
# 表示列を増やしてくれる。
# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラムです。')

# FAQなどで使用されるもの。
# expander1 = st.beta_expander('問い合わせ1')
# expander1.write('問い合わせ1の回答')
# expander2 = st.beta_expander('問い合わせ2')
# expander2.write('問い合わせ2の回答')
# expander3 = st.beta_expander('問い合わせ3')
# expander3.write('問い合わせ3の回答')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition
# --------------------------------------------------------------------------------------
# プログレスバー
st.write('プログレスバー')
'Start!'

# 空にしておいてあとでいじる。
# 表示場所はこの場所になる。
latest_iteration = st.empty()
# 0から100までか、0から1までかを指定する引数。
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
# --------------------------------------------------------------------------------------