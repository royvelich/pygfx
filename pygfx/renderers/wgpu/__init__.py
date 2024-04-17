"""
.. currentmodule:: pygfx.renderers.wgpu


General functions and classes to operate more closely with the wgpu backend.

.. autosummary::
    :toctree: _autosummary/renderers/wgpu
    :template: ../_templates/custom_layout.rst

    print_wgpu_report
    select_power_preference
    select_adapter
    enable_wgpu_features
    WgpuRenderer
    register_wgpu_render_function
    get_shared
    Shared


Classes and functions required to implement custom shaders:

.. autosummary::
    :toctree: _autosummary/renderers/wgpu
    :template: ../_templates/custom_layout.rst

    WorldObjectShader
    Binding
    GfxSampler
    GfxTextureView
    load_wgsl
    shaderlib


Lower level functions that may or may not be needed in custom shaders:

.. autosummary::
    :toctree: _autosummary/renderers/wgpu
    :template: ../_templates/custom_layout.rst

    nchannels_from_format
    to_vertex_format
    to_texture_format

"""

# flake8: noqa

# TODO: \ register_wgpu_render_function to register_wgpu_shader

# Import stuff that people need who create custom shaders, so they can import from pygfx.renderers.wgpu
from ...utils.enums import RenderMask
from .engine.utils import (
    register_wgpu_render_function,
    nchannels_from_format,
    to_vertex_format,
    to_texture_format,
    GfxSampler,
    GfxTextureView,
)
from .engine.shared import (
    Shared,
    get_shared,
    print_wgpu_report,
    select_power_preference,
    select_adapter,
    enable_wgpu_features,
)
from .engine.renderer import WgpuRenderer
from .engine.pipeline import Binding

# Shader classes
from .wgsl import load_wgsl
from .shader.base2 import WorldObjectShader
from .shader._shaderlib import shaderlib

# Load shaders submodules, so that all our builtin shaders become a vailable
from . import shaders
