# runpod-cuda-version-reporter

A tiny RunPod Serverless worker whose *entire job* is to tell you what CUDA version it's running on. That’s it. No frills, no hidden features, no actual productivity value. It’s the digital equivalent of asking, “Hey, you up?” — but for GPUs.

## Useful for:

- Debugging mysterious CUDA version mismatches  
- Verifying whether your container is actually using the base image you *think* it is  
- Poking at RunPod’s serverless runtime just to see if it responds  

## Not useful for:

- Literally anything else

If you’re expecting this to do inference, training, or anything remotely intelligent — it won’t. It prints `nvcc --version` and leaves. A hero’s work.
