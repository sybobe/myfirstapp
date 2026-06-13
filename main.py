import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="⚡",
    layout="centered"
)

pokemon_data = {
    "ISTJ": {
        "pokemon": "이상해씨 🌱",
        "type": "성실한 전략가",
        "desc": "차분하고 책임감이 강한 타입이에요. 맡은 일은 끝까지 해내며, 주변 사람들에게 든든한 안정감을 줍니다."
    },
    "ISFJ": {
        "pokemon": "피카츄 ⚡",
        "type": "따뜻한 보호자",
        "desc": "다정하고 배려심이 많아요. 소중한 사람을 위해 조용히 힘을 내는 사랑스러운 타입입니다."
    },
    "INFJ": {
        "pokemon": "뮤 ✨",
        "type": "신비로운 이상가",
        "desc": "깊은 생각과 따뜻한 마음을 가진 타입이에요. 조용하지만 특별한 영향력을 가지고 있습니다."
    },
    "INTJ": {
        "pokemon": "뮤츠 🧠",
        "type": "천재적인 설계자",
        "desc": "분석력과 계획력이 뛰어나요. 목표를 정하면 누구보다 치밀하게 움직이는 타입입니다."
    },
    "ISTP": {
        "pokemon": "리자몽 🔥",
        "type": "쿨한 해결사",
        "desc": "말보다 행동이 빠른 타입이에요. 위기 상황에서도 침착하게 문제를 해결합니다."
    },
    "ISFP": {
        "pokemon": "이브이 🤎",
        "type": "감성적인 자유인",
        "desc": "부드럽고 자유로운 매력을 가진 타입이에요. 다양한 가능성과 따뜻한 감성을 품고 있습니다."
    },
    "INFP": {
        "pokemon": "토게피 🥚",
        "type": "순수한 몽상가",
        "desc": "상상력이 풍부하고 마음이 따뜻해요. 자신만의 세계와 가치관을 소중히 여깁니다."
    },
    "INTP": {
        "pokemon": "고라파덕 🤯",
        "type": "엉뚱한 철학자",
        "desc": "궁금한 게 많고 생각이 깊은 타입이에요. 가끔 멍해 보여도 머릿속은 누구보다 바쁩니다."
    },
    "ESTP": {
        "pokemon": "꼬부기 😎",
        "type": "장난기 많은 모험가",
        "desc": "에너지가 넘치고 순간 판단력이 좋아요. 어디서든 분위기를 즐겁게 만드는 타입입니다."
    },
    "ESFP": {
        "pokemon": "푸린 🎤",
        "type": "무대 위의 인기스타",
        "desc": "밝고 사랑스러운 매력으로 주변을 즐겁게 해요. 함께 있으면 분위기가 금방 살아납니다."
    },
    "ENFP": {
        "pokemon": "파이리 🔥",
        "type": "열정적인 아이디어 뱅크",
        "desc": "호기심과 에너지가 넘쳐요. 새로운 일에 설레고, 사람들에게 긍정적인 기운을 줍니다."
    },
    "ENTP": {
        "pokemon": "나옹 💰",
        "type": "재치 있는 말재주꾼",
        "desc": "아이디어가 많고 말솜씨가 좋아요. 장난스럽지만 똑똑한 매력을 가진 타입입니다."
    },
    "ESTJ": {
        "pokemon": "잠만보 💤",
        "type": "든든한 현실 관리자",
        "desc": "현실적이고 추진력이 좋아요. 겉으로는 여유로워 보여도 중요한 순간에는 확실히 움직입니다."
    },
    "ESFJ": {
        "pokemon": "럭키 💖",
        "type": "모두의 힐러",
        "desc": "사람을 잘 챙기고 분위기를 따뜻하게 만들어요. 주변 사람들에게 큰 위로가 되는 타입입니다."
    },
    "ENFJ": {
        "pokemon": "라프라스 🌊",
        "type": "따뜻한 리더",
        "desc": "사람들의 마음을 잘 읽고 이끌어주는 타입이에요. 부드럽지만 강한 리더십을 가지고 있습니다."
    },
    "ENTJ": {
        "pokemon": "망나뇽 🐉",
        "type": "카리스마 있는 지휘관",
        "desc": "목표를 향해 강하게 나아가는 타입이에요. 큰 그림을 보고 사람들을 이끄는 힘이 있습니다."
    }
}

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #fff7d6, #e7f5ff);
    }
    .title-box {
        background-color: #ffffffcc;
        padding: 25px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    .result-box {
        background-color: #ffffffdd;
        padding: 30px;
        border-radius: 25px;
        margin-top: 20px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
        text-align: center;
    }
    .pokemon-name {
        font-size: 40px;
        font-weight: bold;
        color: #ff6b6b;
    }
    .type-text {
        font-size: 24px;
        font-weight: bold;
        color: #4dabf7;
    }
    .desc-text {
        font-size: 18px;
        line-height: 1.7;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title-box">
        <h1>⚡ MBTI 포켓몬 추천기 ⚡</h1>
        <p>나의 MBTI와 찰떡궁합인 포켓몬은 누구일까?</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

mbti = st.text_input("MBTI를 입력하세요! 예: INFP, ENTJ, ISFJ", "").upper().strip()

if st.button("🔮 내 포켓몬 찾기"):

    if mbti in pokemon_data:
        result = pokemon_data[mbti]

        st.balloons()

        st.markdown(
            f"""
            <div class="result-box">
                <div class="pokemon-name">{result["pokemon"]}</div>
                <br>
                <div class="type-text">{result["type"]}</div>
                <br>
                <div class="desc-text">{result["desc"]}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.success("추천 완료! 당신과 찰떡인 포켓몬을 찾았어요 🎉")

    elif mbti == "":
        st.warning("MBTI를 먼저 입력해주세요! 예: ENFP")
    else:
        st.error("MBTI는 16가지 유형 중 하나로 입력해주세요. 예: ISTJ, ENFP, INTP")

st.write("")
st.caption("※ 재미용 추천입니다. 진지하게 받아들이면 포켓몬 박사님이 놀랄 수 있어요 😆")
