import numpy as np
from sqlalchemy.orm import Session

from app.db.models import SymptomEmbedding


def add_symptom_embedding(db: Session, uid: int, symptom: str, intensity: float, embedding: list[float]):
    embedding_np = np.asarray(embedding, dtype=np.float32).ravel()
    if embedding_np.size != 384: raise ValueError("Symptom embeddings must be 384-dimensional to match storage.")
    embedding_list = embedding_np.tolist()

    record = SymptomEmbedding(
        user_hmac_id=uid,
        symptom=symptom,
        intensity=intensity,
        embedding=embedding_list
    )

    db.add(record)
    try: db.commit()
    except Exception:
        db.rollback()
        raise
    db.refresh(record)
    return record
