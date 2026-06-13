import streamlit as st

st.set_page_config(
    page_title="MBTI 포켓몬 추천기",
    page_icon="⚡",
    layout="centered"
)

pokemon_data = {
    "ISTJ": {
        "pokemon": "이상해씨",
        "emoji": "🌱",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
        "type": "성실한 전략가",
        "desc": "차분하고 책임감이 강한 타입이에요. 맡은 일은 끝까지 해내며, 주변 사람들에게 든든한 안정감을 줍니다.",
        "good": "꾸준함, 책임감, 현실 감각",
        "tip": "가끔은 계획 밖의 재미도 즐겨보세요!"
    },
    "ISFJ": {
        "pokemon": "피카츄",
        "emoji": "⚡",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "type": "따뜻한 보호자",
        "desc": "다정하고 배려심이 많아요. 소중한 사람을 위해 조용히 힘을 내는 사랑스러운 타입입니다.",
        "good": "배려심, 친절함, 안정감",
        "tip": "남을 챙기는 만큼 나 자신도 챙겨주세요."
    },
    "INFJ": {
        "pokemon": "뮤",
        "emoji": "✨",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png",
        "type": "신비로운 이상가",
        "desc": "깊은 생각과 따뜻한 마음을 가진 타입이에요. 조용하지만 특별한 영향력을 가지고 있습니다.",
        "good": "통찰력, 공감력, 깊은 사고",
        "tip": "생각을 너무 오래 품기보다 표현해보세요."
    },
    "INTJ": {
        "pokemon": "뮤츠",
        "emoji": "🧠",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "type": "천재적인 설계자",
        "desc": "분석력과 계획력이 뛰어나요. 목표를 정하면 누구보다 치밀하게 움직이는 타입입니다.",
        "good": "전략, 분석, 독립성",
        "tip": "완벽한 계획보다 빠른 실행이 답일 때도 있어요."
    },
    "ISTP": {
        "pokemon": "리자몽",
        "emoji": "🔥",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        "type": "쿨한 해결사",
        "desc": "말보다 행동이 빠른 타입이에요. 위기 상황에서도 침착하게 문제를 해결합니다.",
        "good": "순발력, 문제 해결력, 침착함",
        "tip": "가끔은 마음속 생각도 말로 표현해보세요."
    },
    "ISFP": {
        "pokemon": "이브이",
        "emoji": "🤎",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "type": "감성적인 자유인",
        "desc": "부드럽고 자유로운 매력을 가진 타입이에요. 다양한 가능성과 따뜻한 감성을 품고 있습니다.",
        "good": "감성, 유연함, 개성",
        "tip": "좋아하는 것을 더 자신 있게 드러내도 좋아요."
    },
    "INFP": {
        "pokemon": "토게피",
        "emoji": "🥚",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/175.png",
        "type": "순수한 몽상가",
        "desc": "상상력이 풍부하고 마음이 따뜻해요. 자신만의 세계와 가치관을 소중히 여깁니다.",
        "good": "상상력, 진정성, 따뜻함",
        "tip": "꿈을 현실로 옮기는 작은 행동을 시작해보세요."
    },
    "INTP": {
        "pokemon": "고라파덕",
        "emoji": "🤯",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/54.png",
        "type": "엉뚱한 철학자",
        "desc": "궁금한 게 많고 생각이 깊은 타입이에요. 가끔 멍해 보여도 머릿속은 누구보다 바쁩니다.",
        "good": "논리, 호기심, 창의적 사고",
        "tip": "생각만 하지 말고 결과물로 만들어보세요."
    },
    "ESTP": {
        "pokemon": "꼬부기",
        "emoji": "😎",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
        "type": "장난기 많은 모험가",
        "desc": "에너지가 넘치고 순간 판단력이 좋아요. 어디서든 분위기를 즐겁게 만드는 타입입니다.",
        "good": "행동력, 적응력, 자신감",
        "tip": "속도도 좋지만 방향도 함께 확인해보세요."
    },
    "ESFP": {
        "pokemon": "푸린",
        "emoji": "🎤",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/39.png",
        "type": "무대 위의 인기스타",
        "desc": "밝고 사랑스러운 매력으로 주변을 즐겁게 해요. 함께 있으면 분위기가 금방 살아납니다.",
        "good": "친화력, 표현력, 긍정 에너지",
        "tip": "즐거움 속에서도 중요한 약속은 꼭 챙겨보세요."
    },
    "ENFP": {
        "pokemon": "파이리",
        "emoji": "🔥",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
        "type": "열정적인 아이디어 뱅크",
        "desc": "호기심과 에너지가 넘쳐요. 새로운 일에 설레고, 사람들에게 긍정적인 기운을 줍니다.",
        "good": "열정, 창의력, 사람을 끌어당기는 힘",
        "tip": "아이디어를 끝까지 완성하는 연습을 해보세요."
    },
    "ENTP": {
        "pokemon": "나옹",
        "emoji": "💰",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/52.png",
        "type": "재치 있는 말재주꾼",
        "desc": "아이디어가 많고 말솜씨가 좋아요. 장난스럽지만 똑똑한 매력을 가진 타입입니다.",
        "good": "순발력, 토론 능력, 창의성",
        "tip": "재미있는 말 속에도 배려를 살짝 더해보세요."
    },
    "ESTJ": {
        "pokemon": "잠만보",
        "emoji": "💤",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/143.png",
        "type": "든든한 현실 관리자",
        "desc": "현실적이고 추진력이 좋아요. 중요한 순간에는 확실하게 움직이는 믿음직한 타입입니다.",
        "good": "실행력, 책임감, 리더십",
        "tip": "다른 사람의 속도도 함께 존중해보세요."
    },
    "ESFJ": {
        "pokemon": "럭키",
        "emoji": "💖",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/113.png",
        "type": "모두의 힐러",
        "desc": "사람을 잘 챙기고 분위기를 따뜻하게 만들어요. 주변 사람들에게 큰 위로가 되는 타입입니다.",
        "good": "공감, 친절, 관계 관리",
        "tip": "모두를 만족시키려 애쓰지 않아도 괜찮아요."
    },
    "ENFJ": {
        "pokemon": "라프라스",
        "emoji": "🌊",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/131.png",
        "type": "따뜻한 리더",
        "desc": "사람들의 마음을 잘 읽고 이끌어주는 타입이에요. 부드럽지만 강한 리더십을 가지고 있습니다.",
        "good": "리더십, 공감력, 설득력",
        "tip": "남의 기대보다 내 마음의 방향도 살펴보세요."
    },
    "ENTJ": {
        "pokemon": "망나뇽",
        "emoji": "🐉",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/149.png",
        "type": "카리스마 있는 지휘관",
        "desc": "목표를 향해 강하게 나아가는 타입이에요. 큰 그림을 보고 사람들을 이끄는 힘이 있습니다.",
        "good": "추진력, 목표 의식, 결단력",
        "tip": "가끔은 효율보다 감정도 중요할 수 있어요."
    }
}

mbti_list = list(pokemon_data.keys())

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff3c4 0%, #d8f3ff 50%, #ffe0f0 100%);
    }

    .title-box {
        background: rgba(255, 255, 255, 0.85);
        padding: 28px;
        border-radius: 28px;
        text-align: center;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
        margin-bottom: 25px;
    }

    .title-box h1 {
        color: #ff6b6b;
        font-size: 42px;
        margin-bottom: 8px;
    }

    .title-box p {
        color: #444;
        font-size: 18px;
    }

    .result-box {
        background: rgba(255, 255, 255, 0.92);
        padding: 30px;
        border-radius: 28px;
        margin-top: 25px;
        box-shadow: 0px 8px 30px rgba(0,0,0,0.18);
        text-align: center;
    }

    .pokemon-name {
        font-size: 42px;
        font-weight: 800;
        color: #ff6b6b;
        margin-top: 10px;
    }

    .type-text {
        font-size: 25px;
        font-weight: 700;
        color: #228be6;
        margin-bottom: 15px;
    }

    .desc-text {
        font-size: 18px;
        line-height: 1.8;
        color: #333;
        margin-top: 10px;
    }

    .mini-card {
        background-color: #f8f9fa;
        border-radius: 18px;
        padding: 18px;
        margin-top: 14px;
        font-size: 17px;
        color: #333;
        box-shadow: inset 0px 0px 0px 1px rgba(0,0,0,0.05);
    }

    .footer {
        text-align: center;
        color: #666;
        font-size: 14px;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="title-box">
        <h1>⚡ MBTI 포켓몬 추천기 ⚡</h1>
        <p>나의 MBTI와 찰떡궁합인 포켓몬은 누구일까? 🎮</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("🧩 MBTI를 선택해 주세요")

mbti = st.selectbox(
    "직접 입력하지 않아도 돼요!",
    mbti_list,
    index=mbti_list.index("ENFP")
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    button = st.button("🔮 내 포켓몬 찾기", use_container_width=True)

if button:
    result = pokemon_data[mbti]

    st.balloons()

    st.markdown(
        f"""
        <div class="result-box">
            <div style="font-size: 22px;">🎉 당신의 MBTI는 <b>{mbti}</b>!</div>
            <div class="pokemon-name">{result["pokemon"]} {result["emoji"]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.image(result["image"], width=230)

    st.markdown(
        f"""
        <div class="result-box">
            <div class="type-text">✨ {result["type"]} ✨</div>
            <div class="desc-text">{result["desc"]}</div>

            <div class="mini-card">
                <b>🌟 대표 강점</b><br>
                {result["good"]}
            </div>

            <div class="mini-card">
                <b>💡 성장 팁</b><br>
                {result["tip"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("추천 완료! 당신과 찰떡인 포켓몬을 찾았어요 🎈")

else:
    st.info("MBTI를 고른 뒤 버튼을 누르면 포켓몬이 나타나요!")

st.markdown(
    """
    <div class="footer">
        ※ 이 앱은 재미용 MBTI 포켓몬 추천기입니다 😆<br>
        ※ Streamlit Cloud에서 별도 라이브러리 없이 실행 가능합니다.
    </div>
    """,
    unsafe_allow_html=True
)
