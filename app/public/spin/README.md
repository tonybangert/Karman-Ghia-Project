# Turntable frames (Tier B, optional)

Drop sequential photos of the car here (for example 24 to 36 shots taken at
even intervals around it) and add a `spin.json` manifest:

```json
{ "alt": "1965 Karmann Ghia, 360 view", "frames": ["spin/01.jpg", "spin/02.jpg", "..."] }
```

If `spin.json` is absent, the turntable is skipped and the explorer shows the
interactive silhouette only. No placeholder is rendered.
