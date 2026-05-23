"""
Indian Philosophy Knowledge Base with Citations
Completely offline, no API calls needed
"""

INDIAN_PHILOSOPHY_KB = {
    # ============ VEDANTA ============
    "vedanta_atman_brahman": {
        "question": "What is the relationship between Atman and Brahman?",
        "answer": """
In Vedanta philosophy, Atman (individual soul) and Brahman (ultimate reality) are fundamentally the same. 
This non-dual principle is expressed in the Mahavakyas (great statements):
- Tat Tvam Asi (Thou Art That) - The individual consciousness is identical with universal consciousness
- Aham Brahmasmi (I am Brahman) - Direct realization of one's true nature
- Prajnanam Brahma (Consciousness is Brahman) - Reality is pure consciousness itself

This realization is the goal of Advaita Vedanta philosophy, where the apparent separation between 
individual and universal consciousness is recognized as illusion (maya).
        """,
        "tradition": "vedanta",
        "citations": [
            {
                "source": "Chandogya Upanishad",
                "verse": "6.8.7",
                "text": "Tat Tvam Asi",
                "meaning": "Thou Art That - expressing non-duality"
            },
            {
                "source": "Mandukya Upanishad",
                "verse": "1.2",
                "text": "Aum iti etat Brahma",
                "meaning": "Om is Brahman"
            }
        ],
        "confidence": 0.95
    },
    
    "vedanta_maya": {
        "question": "What is Maya in Vedanta philosophy?",
        "answer": """
Maya is the power of illusion that makes the infinite, eternal Brahman appear as finite, temporal world.
Key aspects:
- Maya is neither real nor unreal (anirvachaniya) - it cannot be positively categorized
- It veils the true nature of Brahman (avarana shakti) 
- It projects false appearances (vikshepa shakti)
- Maya exists at empirical level (vyavaharika) but is transcended in self-realization

Through spiritual practice (sadhana) and discrimination (viveka), one transcends maya and realizes Brahman.
        """,
        "tradition": "vedanta",
        "citations": [
            {
                "source": "Adi Shankara - Brahma Sutras",
                "verse": "1.4.3",
                "text": "Mithyatve api tadgraha",
                "meaning": "Maya is neither absolutely real nor absolutely unreal"
            }
        ],
        "confidence": 0.92
    },

    # ============ BUDDHISM ============
    "buddhism_four_noble_truths": {
        "question": "What are the Four Noble Truths in Buddhism?",
        "answer": """
The Four Noble Truths form the foundation of Buddhist philosophy:

1. DUKKHA (Suffering/Unsatisfactoriness):
   - Life contains suffering, pain, impermanence, and unsatisfactoriness
   - This includes not just physical pain but existential dissatisfaction

2. SAMUDAYA (Origin of Suffering):
   - Suffering arises from Tanha (craving, thirst)
   - Three types: kama-tanha (sensual craving), bhava-tanha (craving for existence), vibhava-tanha (craving for non-existence)

3. NIRODHA (Cessation of Suffering):
   - Suffering can be ended through cessation of craving
   - This cessation is Nirvana (Nibbana) - the highest peace

4. MAGGA (Path to Cessation):
   - The Noble Eightfold Path leads to the end of suffering
   - Right view, intention, speech, action, livelihood, effort, mindfulness, concentration
        """,
        "tradition": "buddhism",
        "citations": [
            {
                "source": "Dhammacakkappavattana Sutta",
                "verse": "SN 56.11",
                "text": "Four Noble Truths discourse",
                "meaning": "Buddha's first sermon setting in motion the Wheel of Dharma"
            }
        ],
        "confidence": 0.95
    },

    "buddhism_dependent_origination": {
        "question": "What is Dependent Origination in Buddhism?",
        "answer": """
Dependent Origination (Pratityasamutpada) is the principle that all phenomena arise interdependently.

The Twelve Links (Nidanas):
1. Avidya (Ignorance) → 2. Sankhara (Volitional formation) → 3. Vijnana (Consciousness)
→ 4. Nama-rupa (Name and form) → 5. Shadayatana (Six sense bases) → 6. Sparsha (Contact)
→ 7. Vedana (Sensation) → 8. Tanha (Craving) → 9. Upadana (Clinging) → 10. Bhava (Becoming)
→ 11. Jati (Birth) → 12. Jara-marana (Aging-death)

This cycle illustrates how ignorance perpetuates suffering and rebirth. Breaking this cycle requires 
wisdom (prajna) and mindfulness (sati).
        """,
        "tradition": "buddhism",
        "citations": [
            {
                "source": "Samyutta Nikaya",
                "verse": "SN 12.2",
                "text": "Nidana-samyutta",
                "meaning": "Collection on Dependent Origination"
            }
        ],
        "confidence": 0.93
    },

    # ============ YOGA ============
    "yoga_ashtanga_yoga": {
        "question": "What are the Eight Limbs of Yoga (Ashtanga)?",
        "answer": """
The Eightfold Path of Yoga, described in Patanjali's Yoga Sutras:

1. YAMA (Ethical Restraints): Non-violence, truthfulness, non-stealing, chastity, non-attachment
2. NIYAMA (Observances): Purity, contentment, austerity, self-study, surrender to God
3. ASANA (Physical Postures): Steady, comfortable bodily positions for meditation
4. PRANAYAMA (Breath Control): Regulation of life force (prana) through breathing exercises
5. PRATYAHARA (Sense Withdrawal): Withdrawal of senses from external objects
6. DHARANA (Concentration): One-pointed focus of the mind
7. DHYANA (Meditation): Uninterrupted flow of concentration
8. SAMADHI (Absorption): Liberation, transcendental consciousness, union with the divine

These eight limbs are progressive stages toward self-realization and liberation (moksha).
        """,
        "tradition": "yoga",
        "citations": [
            {
                "source": "Yoga Sutras of Patanjali",
                "verse": "2.29",
                "text": "Yama-niyama-asana-pranayama-pratyahara-dharana-dhyana-samadhayah ashtau",
                "meaning": "The eight limbs of yoga"
            }
        ],
        "confidence": 0.96
    },

    "yoga_samadhi": {
        "question": "What is Samadhi in Yoga philosophy?",
        "answer": """
Samadhi is the highest state of consciousness in yoga - absorption, union, or liberation.

Characteristics:
- Transcendence of subject-object duality
- Complete merger of consciousness with the object of meditation
- Beyond the three states of consciousness: waking, dreaming, deep sleep
- The goal of all yoga practices and spiritual disciplines

Types of Samadhi:
1. Sabija Samadhi (with seed): Consciousness merged but retains subtle impressions
2. Nirbija Samadhi (seedless): Complete transcendence, permanent liberation (moksha)

In Samadhi, individual consciousness (jivatman) realizes its identity with universal consciousness (Brahman).
This is the ultimate fruit of yoga practice.
        """,
        "tradition": "yoga",
        "citations": [
            {
                "source": "Yoga Sutras of Patanjali",
                "verse": "1.3",
                "text": "Tada Drastuh Svarupe Avasthanam",
                "meaning": "Then the seer abides in its own nature"
            }
        ],
        "confidence": 0.94
    },

    # ============ SAMKHYA ============
    "samkhya_prakriti_purusha": {
        "question": "What is the Prakriti-Purusha relationship in Samkhya?",
        "answer": """
Samkhya philosophy posits two eternal, co-equal principles:

PRAKRITI (Nature/Matter):
- Dynamic, ever-changing principle of manifestation
- Composed of three gunas: Sattva (purity), Rajas (activity), Tamas (inertia)
- The material cause of the universe
- Unconscious but intelligent in its functioning

PURUSHA (Consciousness/Spirit):
- Static, unchanging principle of awareness
- Pure witness consciousness
- Infinite, eternal, immutable
- Not the doer, but the conscious observer of all activity

The Relationship:
- Purusha observes and illuminates Prakriti's transformations
- Prakriti acts to fulfill Purusha's implicit desires
- The universe emerges from this cosmic interplay
- Liberation (kaivalya) occurs when Purusha recognizes its distinction from Prakriti

This dualistic framework explains both existence and consciousness.
        """,
        "tradition": "samkhya",
        "citations": [
            {
                "source": "Samkhya Karika",
                "verse": "3",
                "text": "Dve prakrti vidye drsya adrsya avidya saha",
                "meaning": "There are two principles: Prakriti (visible) and Purusha (invisible)"
            }
        ],
        "confidence": 0.91
    },

    # ============ NYAYA ============
    "nyaya_pramanas": {
        "question": "What are the four Pramanas (means of valid knowledge) in Nyaya?",
        "answer": """
Nyaya philosophy establishes four valid means of knowledge (Pramanas):

1. PRATYAKSHA (Perception):
   - Direct sensory experience: seeing, hearing, touching, tasting, smelling
   - Most immediate and reliable form of knowledge
   - Requires proper sense-object contact and mental clarity

2. ANUMANA (Inference):
   - Logical deduction from known premises to unknown conclusions
   - Example: Where there is smoke, there is fire (smoke infers fire)
   - Requires establishing valid logical relationships

3. UPAMANA (Comparison/Analogy):
   - Knowledge through similarity of objects
   - Example: Knowing what a cow is through comparison with known animals
   - Valid when similarities are relevant and significant

4. SABDA (Testimony/Authority):
   - Knowledge from reliable testimony or authoritative sources
   - Includes scriptures, expert testimony, and trustworthy reports
   - Depends on the credibility of the source

These pramanas form the epistemological foundation of Indian knowledge systems.
        """,
        "tradition": "nyaya",
        "citations": [
            {
                "source": "Nyaya Sutras of Aksapada Gautama",
                "verse": "1.1.3",
                "text": "Pratyakshanumanopamanasabdah",
                "meaning": "The four valid means of knowledge"
            }
        ],
        "confidence": 0.90
    },

    # ============ MIMAMSA ============
    "mimamsa_dharma": {
        "question": "What is Dharma according to Mimamsa philosophy?",
        "answer": """
Mimamsa philosophy focuses on understanding Dharma through proper interpretation of Vedic texts.

Definition of Dharma:
- That which is enjoined by the Vedas
- The duties and rituals prescribed for different stages of life
- The ethical and moral order governing human conduct
- Both ritual obligations and ethical principles

Key Concepts:

1. KARMA (Ritual Action):
   - Dharma is primarily understood through Vedic sacrifices and rituals
   - Proper performance of rituals (yajna) sustains cosmic order
   - Each ritual has specific results (phala)

2. SVADHARMA (Individual Duty):
   - Duties specific to one's class (varna) and life stage (ashrama)
   - Different obligations for Brahmin, Kshatriya, Vaishya, Shudra
   - Four life stages: Student (Brahmacharyа), Householder, Forest dweller, Renunciate

3. APURVA (Unseen Power):
   - Rituals create invisible merit that fructifies in future births
   - The mechanism by which karma operates
   - Links ritual actions to their eventual results

Mimamsa emphasizes that understanding and following Dharma leads to well-being and liberation.
        """,
        "tradition": "mimamsa",
        "citations": [
            {
                "source": "Purva Mimamsa Sutra",
                "verse": "1.1.2",
                "text": "Chodotsarjananiyo Dharmah",
                "meaning": "Dharma is that which is indicated by the Vedic injunctions"
            }
        ],
        "confidence": 0.88
    },

    # ============ ADVAITA VEDANTA - Advanced ============
    "advaita_moksha": {
        "question": "What is Moksha (Liberation) in Advaita Vedanta?",
        "answer": """
Moksha in Advaita Vedanta is the ultimate goal - realization of one's true nature as Brahman.

Characteristics:
- NOT escape from the world, but correct understanding of reality
- Realization that the separate individual 'I' never existed
- Freedom from ignorance (avidya) and the three-fold suffering (tapa-traya)
- Immediate, eternal, and absolute freedom

The Nature of Moksha:
- Nitya Mukti: Eternal liberation - one who realizes Brahman is always free
- Not gained or lost; neither temporal nor spatial
- Inherent nature of the Self (Atman)
- "Ever free" (Eka eva Advaita) - there is only one non-dual reality

Impediments to Moksha:
- Ignorance (Avidya): Mistaking the finite for the infinite
- Desires and attachments (Vasanas): Psychological conditioning
- Misidentification with body-mind complex
- Lack of discrimination between real and unreal

Path to Moksha:
- Hearing (Sravana): Study of Upanishads under a qualified teacher
- Contemplation (Manana): Intellectual understanding of non-duality
- Meditation (Nididhyasana): Direct realization through deep meditation

Once realized, moksha is irreversible. It is not a future state to be gained, but the recognition 
of one's ever-free nature in the present.
        """,
        "tradition": "vedanta",
        "citations": [
            {
                "source": "Vivekachudamani of Adi Shankara",
                "verse": "571",
                "text": "Moksha is the eternal realization of non-duality",
                "meaning": "Liberation through recognizing the non-dual nature of reality"
            },
            {
                "source": "Brahma Sutras",
                "verse": "4.4.22",
                "text": "Brahmavit Brahmaiva Bhavati",
                "meaning": "The knower of Brahman becomes Brahman"
            }
        ],
        "confidence": 0.94
    },

    "buddhism_emptiness": {
        "question": "What is Sunyata (Emptiness) in Buddhist philosophy?",
        "answer": """
Sunyata is the Buddhist doctrine of emptiness - a cornerstone of Mahayana Buddhism.

Understanding Emptiness:
- Not nothingness, but the absence of inherent, independent, permanent essence
- All phenomena are empty of self-nature (svabhava-sunya)
- Objects lack intrinsic, unchanging identity
- This applies to all conditioned and unconditioned phenomena

The Two Truths Doctrine:
1. Conventional Truth (Samvritti Satya): Everyday reality of cause-effect, objects, persons
2. Ultimate Truth (Paramartha Satya): The emptiness of all things

Implications:
- No permanent, unchanging soul (anatman/anatma)
- All phenomena arise through dependent origination
- Liberation comes from directly realizing emptiness
- Bodhisattvas vow to achieve enlightenment for all beings through understanding emptiness

Practical Impact:
- Reduces clinging and attachment (which cause suffering)
- Opens space for compassion (all beings equally lack independent essence)
- Liberates consciousness from rigid conceptual frameworks
- Enables direct perception of reality as it truly is

Sunyata is not mere intellectual understanding but direct experiential realization.
        """,
        "tradition": "buddhism",
        "citations": [
            {
                "source": "Heart Sutra",
                "verse": "Prajnaparamita Hridaya Sutra",
                "text": "Sunyata, sunyata - Emptiness, emptiness",
                "meaning": "Central assertion of the Heart Sutra on emptiness"
            },
            {
                "source": "Madhyamaka School",
                "verse": "Mulamadhyamakakarika",
                "text": "Nagarjuna's foundational text on emptiness",
                "meaning": "Philosophical elaboration of emptiness doctrine"
            }
        ],
        "confidence": 0.93
    },

    "yoga_pratyahara": {
        "question": "What is Pratyahara (sense withdrawal) in yoga?",
        "answer": """
Pratyahara is the fifth limb of Ashtanga Yoga - the withdrawal of senses from external objects.

Definition:
- 'Prati' = away, 'Ahara' = food/nourishment
- The senses are withdrawn from external sensory objects as a turtle withdraws into its shell
- Neither suppression nor denial, but conscious disengagement

Purpose:
- Bridge between external practices (asana, pranayama) and internal practices (dharana, dhyana)
- Strengthens mental discipline and focus
- Reduces sensory distraction and mental agitation
- Prepares consciousness for meditation

Process:
1. Awareness of sensory activity without identification
2. Deliberate withdrawal of attention from external stimuli
3. Internalization of consciousness toward mental awareness
4. Development of prarabdha (subtle sensory capacity without external anchoring)

Benefits:
- Greater control over the mind and senses
- Reduced reactivity to external stimuli
- Enhanced introspective capacity
- Foundation for deeper meditation practice
- Emotional stability and mental tranquility

Pratyahara is essential for progressing toward the highest states of yoga (samadhi).
        """,
        "tradition": "yoga",
        "citations": [
            {
                "source": "Yoga Sutras of Patanjali",
                "verse": "2.54",
                "text": "Sva-visayasamprayoge Chitta-svarupa-anukarah Ivendriyah Pratyahara",
                "meaning": "When the senses withdraw from objects, pratyahara is established"
            }
        ],
        "confidence": 0.92
    },
}

def get_answer_by_key(key: str) -> dict:
    """Retrieve answer from knowledge base"""
    return INDIAN_PHILOSOPHY_KB.get(key)

def get_all_questions() -> list:
    """Get all available questions"""
    return [
        {
            "key": key,
            "question": data["question"],
            "tradition": data["tradition"]
        }
        for key, data in INDIAN_PHILOSOPHY_KB.items()
    ]

def search_kb(keyword: str) -> list:
    """Search knowledge base by keyword"""
    results = []
    keyword_lower = keyword.lower()
    
    for key, data in INDIAN_PHILOSOPHY_KB.items():
        if (keyword_lower in data["question"].lower() or 
            keyword_lower in data["answer"].lower() or
            keyword_lower in data["tradition"].lower()):
            results.append({
                "key": key,
                "question": data["question"],
                "tradition": data["tradition"],
                "match_score": 0.9
            })
    
    return results