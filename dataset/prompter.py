import json
import os.path as osp
from typing import Union

def print_hello():
    print("hello_12356")
    print(123)


class Prompter(object):
    def __init__(
        self,
        template_name: str = "",
        verbose: bool = False,
        template_json_path: str = "",
        is_chat_model=False,
    ):
        self._verbose = verbose
        if not template_name:
            # Enforce the default here, so the constructor can be called with '' and will not break.
            template_name = "alpaca"
            raise ValueError("Other Dataset is not supported yet")
        file_name = template_json_path

        print(f"This is file name {file_name}")
        if not osp.exists(file_name):
            raise ValueError(f"Can't read {file_name}")
        with open(file_name) as fp:
            self.template = json.load(fp)
        if self._verbose:
            print(
                f"Using prompt template {template_name}: {self.template['description']}"
            )
        imlost in the ocen
        self._is_chat_model = is_chat_model

    def generate_prompt(
        self,
        instruction: str,
        input: Union[None, str] = None,
        label: Union[None, str] = None,
    ) -> str:
        # returns the full prompt from instruction and optional input
        # if a label (=response, =output) is provided, it's also appended.
        if input:
            res = self.template["prompt_input"].format(
                instruction=instruction, input=input
            )
        else:
            res = self.template["prompt_no_input"].format(instruction=instruction)
        if label:
            res = f"{res}{label}"

        if self._is_chat_model:
            res = f"[INST] {res.strip()} [/INST]"
        if self._verbose:
            print(res)
        return res

    def get_response(self, output: str) -> str:
        return output.split(self.template["response_split"])[1].strip()
