#! /usr/bin/env python

from pathlib import Path


ROOT = Path(__file__).resolve().parent


def generate(template_file, prefix_list):
    template_path = ROOT / template_file
    with open(template_path, "r", encoding="utf-8") as f:
        template_text = f.read()

    for prefix in prefix_list:
        if prefix == "":
            output_file = ROOT / template_file.replace(".in", "")
        else:
            output_file = ROOT / template_file.replace(".in", "_" + prefix.rstrip("/"))

        output_text = template_text.format(PREFIX=prefix)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output_text)

        print(f"Generated: {output_file}")


prefix_list = ["", "left/", "right/"]
generate("fairino3_v6_integrated_specific_config.in.xml", prefix_list)
generate("fairino3_v6_integrated_body.in.xml", prefix_list)
