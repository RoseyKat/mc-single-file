import json
import os
import platform

def clear():
    '''Clear terminal'''
    a = platform.system()
    if a == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def compile_common(file, obj):
    with open(file, "r") as f:
        data = json.loads(f.read())
        indent = data["type"]["indent"]

    if obj == "texts":
        lang_data = data["texts"]

        # Compile languages.json
        os.makedirs("output/RP/texts", exist_ok=True)
        with open("output/RP/texts/languages.json", "w") as f:
            f.write("[]")

        texts = []
        for i in lang_data:
            texts += [i["language"]]

        with open("output/RP/texts/languages.json", "w") as f:
            f.write(json.dumps(texts, indent=indent))

        # Compile lang files
        for i in lang_data:
            trans_key = i["translation"]
            language = i["language"]

            # Check if .lang file doesn't already exist, as to not erase everything in the file.
            if os.path.exists(f"output/RP/texts/{language}.lang"):
                with open(f"output/RP/texts/{language}.lang", "a") as f:
                    f.write(f"\n{trans_key}")
            
            else:
                with open(f"output/RP/texts/{language}.lang", "w") as f:
                    f.write(f"{trans_key}")

def compile_entity(file):
    with open(file, "r") as f:
        data = json.loads(f.read())

    ignore_list = data["type"]["ignore"]
    indent = data["type"]["indent"]
    name = str(os.path.basename(file))

    # Compile server
    if "server" in ignore_list:
        print("Ignored: server")
    else:
        os.makedirs("output/BP/entities", exist_ok=True)
        server_entity = data["server"]
        with open(f"output/BP/entities/{name}", "w") as f:
            f.write(json.dumps(server_entity, indent=indent))

    # Compile client
    if "client" in ignore_list:
        print("Ignored: client")
    else:
        os.makedirs("output/RP/entity", exist_ok=True)
        client_entity = data["client"]
        with open(f"output/RP/entity/{name}", "w") as f:
            f.write(json.dumps(client_entity, indent=indent))

    # Compile render controller
    if "render_controller" in ignore_list:
        print("Ignored: render_controller")
    else:
        os.makedirs("output/RP/render_controllers", exist_ok=True)
        render_controller = data["render_controller"]
        with open(f"output/RP/render_controllers/{name}", "w") as f:
            f.write(json.dumps(render_controller, indent=indent))

    # Compile animations
    if "animation" in ignore_list:
        print("Ignored: animation")
    else:
        os.makedirs("output/RP/animations", exist_ok=True)
        animation = data["animation"]
        with open(f"output/RP/animations/{name}", "w") as f:
            f.write(json.dumps(animation, indent=indent))

    # Compile animation controllers
    if "animation_controller" in ignore_list:
        print("Ignored: animation_controller")
    else:
        os.makedirs("output/RP/animation_controllers", exist_ok=True)
        animation_controller = data["animation_controller"]
        with open(f"output/RP/animation_controllers/{name}", "w") as f:
            f.write(json.dumps(animation_controller, indent=indent))

    # Compile geometry
    if "geometry" in ignore_list:
        print("Ignored: geometry")
    else:
        os.makedirs("output/RP/geometry/entity", exist_ok=True)
        geometry = data["geometry"]
        with open(f"output/RP/geometry/entity/{name.replace('.json', '')}.geo.json", "w") as f:
            f.write(json.dumps(geometry, indent=indent))

    # Compile texts
    if "texts" in ignore_list:
        print("Ignored: texts")
    else:
        compile_common(file, "texts")

def process_file(file):
    with open(file, "r") as f:
        data = json.loads(f.read())

    if data["type"]["file_type"] == "entity":
        compile_entity(file)

process_file("BP/example_entity.json")