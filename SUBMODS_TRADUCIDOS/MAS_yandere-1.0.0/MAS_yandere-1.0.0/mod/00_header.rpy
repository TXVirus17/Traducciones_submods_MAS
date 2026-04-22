    init -990 python in mas_submod_utils:
        Submod(
            author="otter",
            name="MAS Yandere Submod",
            description="Este mod convierte a Monika en una yandere, para que el jugador viva la experiencia de una relación tóxica tal y como se ve en el tropo del anime, (Traducción por TX_Virus). ",
            version="1.0.0",
            dependencies={},
            settings_pane=None,
            version_updates={
            }
        )

    init -989 python:
        if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
            store.sup_utils.SubmodUpdater(
                submod="MAS Yandere Submod",
                user_name="my-otter-self",
                repository_name="mas_yandere",
                submod_dir="/Submods/MAS Yandere Submod",
                extraction_depth=3,
                redirected_files=(
                    "README.md",
                    "LICENSE.txt"
                )
            )
