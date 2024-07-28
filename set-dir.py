import os

# Define the folder structure
folders = {
    "AI-Character-Simulator-Tutorial": [
        "1_introduction",
        "2_LLM_understanding",
        "3_virtual_character_creation",
        "4_text_to_speech",
        "5_renpy_basics",
        "6_advanced_LLM_TTS",
        "7_API_integration",
        "8_simulator_project",
        "9_finalization_deployment"
    ],
    "2_LLM_understanding": [
        "1_LLM_concept_history",
        "2_main_LLM_intro",
        "3_LLM_mechanics",
        "4_LLM_API_usage",
        "5_LLM_API_practice"
    ],
    "3_virtual_character_creation": [
        "1_character_concept",
        "2_image_generation_models",
        "3_prompt_engineering",
        "4_stable_diffusion_usage",
        "5_midjourney_usage",
        "6_prompt_practice"
    ],
    "4_text_to_speech": [
        "1_TTS_concept",
        "2_main_TTS_models",
        "3_good_voice_data",
        "4_whisper_API",
        "5_other_TTS_API",
        "6_TTS_API_practice"
    ],
    "6_advanced_LLM_TTS": [
        "1_LLM_finetuning",
        "2_TTS_finetuning",
        "3_finetuning_practice"
    ],
    "7_API_integration": [
        "1_LLM_integration",
        "2_TTS_integration",
        "3_integration_practice"
    ],
    "8_simulator_project": [
        "1_project_planning",
        "2_character_scenario",
        "3_dialogue_scenario",
        "4_voice_synthesis",
        "5_interactive_game",
        "6_interaction_practice"
    ],
    "9_finalization_deployment": [
        "1_project_debugging",
        "2_game_build",
        "3_additional_features",
        "4_summary_QA"
    ]
}

# Define the files to create in each folder
files = {
    "1_introduction": ["README.md", "setup_guide.md"],
    "2_LLM_understanding/5_LLM_API_practice": ["example_api_call.py", "response_handling.py"],
    "3_virtual_character_creation/6_prompt_practice": ["prompt_examples.md"],
    "4_text_to_speech/6_TTS_API_practice": ["whisper_example.py"],
    "6_advanced_LLM_TTS/3_finetuning_practice": ["LLM_finetuning.py", "TTS_finetuning.py"],
    "7_API_integration/3_integration_practice": ["api_integration.py"],
    "8_simulator_project/6_interaction_practice": ["game_interaction.py"]
}

# Create the folders and files
for parent, subfolders in folders.items():
    parent_path = os.path.join("AI-Character-Simulator-Tutorial", parent) if parent != "AI-Character-Simulator-Tutorial" else parent
    for subfolder in subfolders:
        os.makedirs(os.path.join(parent_path, subfolder), exist_ok=True)

    if parent in files:
        for file in files[parent]:
            with open(os.path.join(parent_path, file), 'w') as f:
                f.write(f"# {file}\n")

# Create files in specific subfolders
for subfolder, subfiles in files.items():
    subfolder_path = os.path.join("AI-Character-Simulator-Tutorial", subfolder)
    for subfile in subfiles:
        with open(os.path.join(subfolder_path, subfile), 'w') as f:
            f.write(f"# {subfile}\n")

# Create main README.md file
with open(os.path.join("AI-Character-Simulator-Tutorial", "README.md"), 'w') as f:
    f.write("# AI Character Simulator Tutorial\n")
