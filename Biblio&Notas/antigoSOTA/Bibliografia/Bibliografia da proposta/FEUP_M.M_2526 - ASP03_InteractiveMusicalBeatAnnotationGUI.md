# Proposal: Interactive Musical Beat Annotation GUI

## Context of the proposal

Computational rhythm analysis is fundamental to Music Information Retrieval (MIR), focusing on extracting rhythmic information from audio signals (Müller, 2015). Beat tracking, which identifies the underlying beat structure of musical pieces, is essential for applications like interactive music systems, audio-visual synchronization, and automatic transcription.

Current state-of-the-art beat tracking methods, predominantly based on neural networks (CNNs, TCNs, Transformers), achieve excellent performance (F1-scores >0.9) on steady 4/4 rhythms with percussive textures but struggle with expressive music, complex meters, and non-percussive textures, often achieving accuracy below 0.5. These limitations stem from dependence on large annotated datasets and poor generalization to unseen musical complexities.

The Annotation Gap: The current de facto standard for musical beat annotation relies on a standalone open-source desktop application: Sonic Visualiser. While powerful and widely adopted in the research community, this tool presents significant limitations: it lacks collaborative features, offers limited interactive feedback, and provides no machine learning integration for annotation assistance. This creates a clear opportunity to advance beyond traditional desktop-based annotation workflows.

The field would benefit from modern web-based annotation tools that leverage contemporary technologies like Wavesurfer.js integrated into React-based interfaces, that provide real-time ML feedback. Such tools could incorporate signal processing or interactive machine learning techniques to provide intelligent annotation suggestions, addressing the cold-start problem while maintaining user control and expertise. Alternatively, advancing Sonic Visualiser's Qt/C++ architecture with modern ML integration capabilities could enhance the existing ecosystem while preserving familiar workflows.

Human-in-the-Loop (HITL) approaches have shown promise in various domains, but current musical annotation workflows remain largely isolated from machine learning advances. This proposal aims to bridge this gap by creating an integrated annotation ecosystem that combines modern technologies with interactive machine learning.

## Goals

1. Modernize Annotation Infrastructure: Develop a contemporary web-based annotation system or advance the existing Sonic Visualiser framework, incorporating collaborative features and real-time feedback and interaction mechanisms that surpass current standalone tool limitations.

2. As part of the system architecture phase, a Python wireframe library will be shared early in the project to visualise and test annotation concepts, enabling community feedback before final interface decisions.

3. Integrate Self-Supervised Learning: Implement self-supervised learning (SSL) techniques that provide intelligent annotation suggestions without requiring extensive pre-labeled datasets, addressing the cold-start problem effectively.

4. Create Interactive ML Feedback Loops: Design user-centric iteration mechanisms where user annotations inform model refinement in real-time, creating a symbiotic human-machine annotation process.

5. Validate Through User Studies: Conduct comprehensive testing with diverse users (musicologists, producers, researchers) to assess effectiveness, usability, and accuracy improvements across various musical scenarios.

6. Open Source Impact: Contribute to the research community through GitHub repositories and libraries, potentially integrating with existing frameworks like Gradio or Hugging Face, and target publication at conferences like Intelligent User Interfaces (IUI), ACM Multimedia or International Society for Music Information Retrieval (ISMIR).

## Innovative Aspects

1. Enhanced Annotation Experience: Move beyond traditional desktop-bound annotation workflows by creating an integrated system that actively engages users in semi-automatic annotation processes, leveraging modern technologies for improved collaboration and accessibility.

2. Intelligent Visual Feedback: Develop interactive interfaces where signal processing techniques (e.g. tempo grid alignment, onset detection) and ML model outputs (e.g. beat activation functions) are dynamically visualized alongside user annotations, providing immediate visual correlation and conflict detection.

3. Bidirectional Learning: Create a system where user expertise refines ML models in real-time while ML predictions inform and accelerate user annotation decisions, establishing an effective human-machine collaboration workflow.

4. Cold-Start Mitigation: Implement streamlined workflows for annotating challenging musical excerpts, using SSL techniques to bootstrap model performance from minimal initial annotations.

## Workplan

1. Technology Landscape Analysis: Evaluate current annotation tools (Sonic Visualiser, Audacity, web-based alternatives) and identify specific technical and user experience limitations that create opportunities for innovation.

2. User-Centered Design Research: Interview current annotators, conduct usability studies on existing tools, and identify specific pain points and desired features for modern annotation workflows.

3. Initial Visualisation Prototype Library: Develop a Python-based wireframe toolkit using matplotlib and librosa for rapid prototyping and evaluation of key visualisation components. This early-stage library will support: display of waveforms and spectrograms with overlaid beat annotations, visual alignment of tempo grids and activation functions, overlay of user annotations versus ML suggestions with clear conflict/agreement markers.

4. System Architecture Development: Design and implement either a React-based web application with Wavesurfer.js integration or enhancements to Sonic Visualiser's Qt/C++ architecture, incorporating SSL model integration and modern interaction paradigms.

5. Interactive ML Integration: Develop real-time feedback mechanisms where user annotations immediately influence model predictions and vice versa, creating responsive annotation assistance.

6. Comprehensive Evaluation: Test the system with diverse user groups, measure annotation efficiency improvements, and assess accuracy gains compared to traditional workflows.

7. Community Contribution: Open-source the developed system, create comprehensive documentation, and promote and present it at a relevant international conference.

## Bibliography
Böck, S., & Davies, M. E. P. (2020). Deconstruct, Analyse, Reconstruct: How To Improve Tempo, Beat, and Downbeat Estimation. Proceedings of the 21st International Society for Music Information Retrieval Conference (ISMIR), 574–582.


Desblancs, D., Lostanlen, V., & Hennequin, R. (2023). Zero-Note Samba: Self-Supervised Beat Tracking. IEEE/ACM Transactions on Audio, Speech, and Language Processing, 31, 2922–2934. https://doi.org/10.1109/TASLP.2023.3297963


Driedger, J., Schreiber, H., De Haas, W. B., & Müller, M. (2019). Towards automatically correcting tapped beat annotations for music recordings. Proceedings of the 20th International Society for Music Information Retrieval Conference (ISMIR), 200–207.


Hung, Y. N., Wang, J. C., Song, X., Lu, W. T., & Won, M. (2022). Modeling Beats and Downbeats With a Time-Frequency Transformer. ICASSP, IEEE International Conference on Acoustics, Speech and Signal Processing - Proceedings, 2022-May, 401–405. https://doi.org/10.1109/ICASSP43922.2022.9747048


Koops, H. V., Micchi, G., Manco, I., & Quinton, E. (2023). Serenade: A Model for Human-in-the-loop Automatic Chord Estimation. http://arxiv.org/abs/2310.11165


Müller, M. (2015). Fundamentals of Music Processing. Springer International Publishing. https://doi.org/10.1007/978-3-319-21945-5


Pinto, A., Böck, S., Cardoso, J., & Davies, M. (2021). User-Driven Fine-Tuning for Beat Tracking. Electronics, 10(13), 1518. https://doi.org/10.3390/electronics10131518


Pinto, A. S., & Bernardes, G. (2023). Bridging the Rhythmic Gap: A User-Centric Approach to Beat Tracking in Challenging Music Signals. 16th International Symposium on Computer Music Multidisciplinary Research (CMMR), 1–12.


Pinto, A. S., Domingues, I., & Davies, M. E. P. (2020). Shift If You Can: Counting and Visualising Correction Operations for Beat Tracking Evaluation. Extended Abstracts for the Late-Breaking Demo Session of the International Society for Music Information Retrieval Conference (ISMIR).


Yamamoto, K. (2021). Human-in-the-Loop Adaptation for Interactive Musical Beat Tracking. Proceedings of the 22nd International Society for Music Information Retrieval Conference (ISMIR). 

## Related Conferences and Journals
Intelligent User Interfaces (IUI), ACM Multimedia or International Society for Music InformationRetrieval (ISMIR).


## Additional Information
This dissertation will be conducted remotely or at the Sound and Music Computing Lab (SMC Lab) at FEUP, depending on the student’s preference. The lab provides a collaborative research setting with access to shared resources, musical datasets, and ongoing projects. Students will have opportunities to interact with peers working on related dissertations and with experienced researchers in rhythm analysis and Music Information Retrieval.

The proposal is part of a broader research initiative focused on computational rhythm analysis. While this dissertation targets the human annotation experience through interactive systems and interface design, complementary work within the initiative addresses core machine learning challenges such as generalisation and data efficiency. This coordinated approach ensures that results across different strands can inform and strengthen one another.

# Student Profile (not included in the proposal)
- Interest in audio processing and music technology; a musical background (performance, composition, or theory) is preferred.
- Proficient in Python, with experience in Librosa, NumPy, or similar audio libraries. Experience with JavaScript/React or Qt/PyQt is a plus.
- Familiar with open-source workflows, including Git/Github.
- Motivated by research, with interest in publishing and contributing to open-source tools.
- Collaborative and comfortable working in a lab setting with users such as musicologists and producers.