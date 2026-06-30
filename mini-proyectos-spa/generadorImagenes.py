import torch
from diffusers import LCMScheduler, AutoPipelineForText2Image

model_id = "Lykon/dreamshaper-7"
adapter_id = "latent-consistency/lcm-lora-sdv1-5"

pipe = AutoPipelineForText2Image.from_pretrained(model_id, torch_dtype=torch.float16, variant="fp16")
pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)

pipe.to("cpu") #si no tienes GPU
#pipe.to("cuda") #si tinenes GPU
#pipe.to("mps") #para Mac con procesadores M

pipe.safety_checker = None
pipe.feature_extractor = None

# Cargar y fusionar lcm lora
pipe.load_lora_weights(adapter_id)
pipe.fuse_lora()

prompt = "An image of a sunset over the sea."

# Desactivar guidance_scale pasando 0
image = pipe(prompt=prompt, num_inference_steps=4, guidance_scale=0).images[0]

# --- AQUÍ TIENES LA LÍNEA PARA GUARDAR ---
image.save("imagen.png")

print("Imagen generada y guardada correctamente")
