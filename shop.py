import streamlit as st

# 1. Настройка вкладки браузера
st.set_page_config(page_title="Мой Кликер", page_icon="🚀")

st.title("Моя игра")

# 2. Память игры
if "monay" not in st.session_state:
  st.session_state.monay = 0
if "power" not in st.session_state:
  st.session_state.power = 1
if "price1" not in st.session_state:
  st.session_state.price1 = 50
if "price2" not in st.session_state:
  st.session_state.price2 = 450
if "auto_power" not in st.session_state:
  st.session_state.auto_power = 0
if "shop_open" not in st.session_state:
  st.session_state.shop_open = False

price3 = 1000

# 3. Главная кнопка клика
if st.button("Пополнить баланс 🚀"):
  st.session_state.monay += st.session_state.power


# 4. Блок баланса и автокликера
@st.fragment(run_every=1)
def show_stats():
  if st.session_state.auto_power > 0:
    st.session_state.monay += st.session_state.auto_power

  st.write(f"Ваш баланс: **{st.session_state.monay}** монет")
  st.write(
      f"Монет за клик: **{st.session_state.power}** | Автодоход:"
      f" **{st.session_state.auto_power}/сек**"
  )


show_stats()

# 5. Кнопка открытия и закрытия магазина
if st.button("Магазин 🛒"):
  st.session_state.shop_open = not st.session_state.shop_open

# 6. Товары в магазине
if st.session_state.shop_open:
  shoping1, shoping2, shoping3 = st.columns(3)

  with shoping1:
    if st.button(f"Множитель ({st.session_state.price1})"):
      if st.session_state.monay >= st.session_state.price1:
        st.session_state.monay -= st.session_state.price1
        st.session_state.power += 1
        st.session_state.price1 += 20
        st.session_state.price2 += 100  # мега-множитель тоже дорожает!
        st.session_state.shop_open = False
        st.toast("Куплен множитель! +1 к клику ⚡")
        st.rerun()
      else:
        st.toast("У вас недостаточно денег ❌")

  with shoping2:
    if st.button(f"Мега-множитель х5 ({st.session_state.price2})"):
      if st.session_state.monay >= st.session_state.price2:
        st.session_state.monay -= st.session_state.price2
        st.session_state.power *= 5
        st.session_state.price2 *= 3  # цена х5 растет после покупки
        st.session_state.shop_open = False
        st.toast("Куплен мега-множитель! 🔥")
        st.rerun()
      else:
        st.toast("У вас недостаточно денег ❌")

  with shoping3:
    if st.button(f"Авто кликер ({price3})"):
      if st.session_state.monay >= price3:
        st.session_state.monay -= price3
        st.session_state.auto_power += 5
        st.session_state.shop_open = False
        st.toast("Куплен авто кликер! +5 монет/сек 🤖")
        st.rerun()
      else:
        st.toast("У вас недостаточно денег ❌")
if st.button(".", type="tertiary"):
        if not st.session_state.get("egg_used", False):
            st.session_state.monay += 350
            st.session_state.egg_used = True
            st.toast("Тайник найден! +350 монет 🎁")
            st.balloons()
            st.rerun()
