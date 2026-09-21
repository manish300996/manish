# LinkedIn post images

1080×1080 cover + three 1080×1350 (4:5) graphics. Upload as a **carousel** (4 images) or pick one.

| File | Use |
|---|---|
| `00_cover_square.png` | Cover / first slide |
| `01_six_boxes.png` | Framework (best single image) |
| `02_unglamorous_half.png` | Checklist |
| `03_looks_like_vs_is.png` | Before / after |

Caption (with carousel or with `01` only):

```
A data engineer’s job is not “move data from A to B”.
It is making the same number show up tomorrow — after late data, a schema change, and a backfill.

Grain. Incremental. Batch vs CDC. Replayable DAGs. Tests before gold. Spark UI before a bigger cluster.

SQL + Python + Spark still do most of the work.
The rest is discipline, not another logo.

#DataEngineering #ApacheSpark #dbt #DataQuality
```

Regenerate: `python3 linkedin-posts/make_images.py`
