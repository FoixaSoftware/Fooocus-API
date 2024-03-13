from typing import Dict, List, Tuple
import numpy as np

from modules import config


def get_aspect_ratio_value(label: str) -> str:
    return label.split(' ')[0].replace('×', '*')


default_inpaint_engine_version = config.default_inpaint_engine_version
default_styles = config.default_styles
default_base_model_name = config.default_base_model_name
default_refiner_model_name = config.default_refiner_model_name
default_refiner_switch = config.default_refiner_switch
default_loras = config.default_loras
default_cfg_scale = config.default_cfg_scale
default_prompt_negative = config.default_prompt_negative
default_sampler = config.default_sampler
default_scheduler = config.default_scheduler

default_aspect_ratio = get_aspect_ratio_value(config.default_aspect_ratio)
available_aspect_ratios = [get_aspect_ratio_value(a) for a in config.available_aspect_ratios]

uov_methods = [
    'Disabled', 'Vary (Subtle)', 'Vary (Strong)', 'Upscale (1.5x)',
    'Upscale (2x)', 'Upscale (Fast 2x)', 'Upscale (Custom)'
]

outpaint_expansions = [
    'Left', 'Right', 'Top', 'Bottom'
]


class ImageGenerationParams:
    """Parameters for image generation"""

    def __init__(self, prompt: str,
                 negative_prompt: str,
                 style_selections: List[str],
                 performance_selection: str,
                 aspect_ratios_selection: str,
                 image_number: int,
                 image_seed: int | None,
                 sharpness: float,
                 guidance_scale: float,
                 base_model_name: str,
                 refiner_model_name: str,
                 refiner_switch: float,
                 loras: List[Tuple[str, float]],
                 uov_input_image: np.ndarray | None,
                 uov_method: str,
                 upscale_value: float | None,
                 outpaint_selections: List[str],
                 outpaint_distance_left: int,
                 outpaint_distance_right: int,
                 outpaint_distance_top: int,
                 outpaint_distance_bottom: int,
                 inpaint_input_image: Dict[str, np.ndarray] | None,
                 inpaint_additional_prompt: str | None,
                 image_prompts: List[Tuple[np.ndarray, float, float, str]],
                 advanced_params: List[any] | None,
                 require_base64: bool):
        self.prompt = prompt
        self.negative_prompt = negative_prompt
        self.style_selections = style_selections
        self.performance_selection = performance_selection
        self.aspect_ratios_selection = aspect_ratios_selection
        self.image_number = image_number
        self.image_seed = image_seed
        self.sharpness = sharpness
        self.guidance_scale = guidance_scale
        self.base_model_name = base_model_name
        self.refiner_model_name = refiner_model_name
        self.refiner_switch = refiner_switch
        self.loras = loras
        self.uov_input_image = uov_input_image
        self.uov_method = uov_method
        self.upscale_value = upscale_value
        self.outpaint_selections = outpaint_selections
        self.outpaint_distance_left = outpaint_distance_left
        self.outpaint_distance_right = outpaint_distance_right
        self.outpaint_distance_top = outpaint_distance_top
        self.outpaint_distance_bottom = outpaint_distance_bottom
        self.inpaint_input_image = inpaint_input_image
        self.inpaint_additional_prompt = inpaint_additional_prompt
        self.image_prompts = image_prompts
        self.require_base64 = require_base64

        if advanced_params is None:
            disable_preview = False
            adm_scaler_positive = 1.5
            adm_scaler_negative = 0.8
            adm_scaler_end = 0.3
            adaptive_cfg = 7.0
            sampler_name = default_sampler
            scheduler_name = default_scheduler
            generate_image_grid = False
            overwrite_step = -1
            overwrite_switch = -1
            overwrite_width = -1
            overwrite_height = -1
            overwrite_vary_strength = -1
            overwrite_upscale_strength = -1
            mixing_image_prompt_and_vary_upscale = False
            mixing_image_prompt_and_inpaint = False
            debugging_cn_preprocessor = False
            skipping_cn_preprocessor = False
            controlnet_softness = 0.25
            canny_low_threshold = 64
            canny_high_threshold = 128
            refiner_swap_method = 'joint'
            freeu_enabled = False
            freeu_b1, freeu_b2, freeu_s1, freeu_s2 = [None] * 4
            debugging_inpaint_preprocessor = False
            inpaint_disable_initial_latent = False
            inpaint_engine = default_inpaint_engine_version
            inpaint_strength = 1.0
            inpaint_respective_field = 0.618
            inpaint_mask_upload_checkbox = False
            invert_mask_checkbox = False
            inpaint_erode_or_dilate = 0

            # Auto set mixing_image_prompt_and_inpaint to True
            if len(self.image_prompts) > 0 and inpaint_input_image is not None:
                print('Mixing Image Prompts and Inpaint Enabled')
                mixing_image_prompt_and_inpaint = True
            if len(self.image_prompts) > 0 and uov_input_image is not None:
                print('Mixing Image Prompts and Vary Upscale Enabled')
                mixing_image_prompt_and_vary_upscale = True

            self.advanced_params = [
                disable_preview, adm_scaler_positive, adm_scaler_negative, adm_scaler_end,
                adaptive_cfg, sampler_name, scheduler_name, generate_image_grid,
                overwrite_step, overwrite_switch, overwrite_width, overwrite_height,
                overwrite_vary_strength, overwrite_upscale_strength,
                mixing_image_prompt_and_vary_upscale, mixing_image_prompt_and_inpaint,
                debugging_cn_preprocessor, skipping_cn_preprocessor, controlnet_softness,
                canny_low_threshold, canny_high_threshold, refiner_swap_method,
                freeu_enabled, freeu_b1, freeu_b2, freeu_s1, freeu_s2,
                debugging_inpaint_preprocessor, inpaint_disable_initial_latent,
                inpaint_engine, inpaint_strength, inpaint_respective_field,
                inpaint_mask_upload_checkbox, invert_mask_checkbox, inpaint_erode_or_dilate
            ]
        else:
            self.advanced_params = advanced_params
