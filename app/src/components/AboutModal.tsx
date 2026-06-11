import { Modal } from './Modal'
import { useArchive } from '@/lib/useArchive'

export function AboutModal({ open, onClose }: { open: boolean; onClose: () => void }) {
  const a = useArchive()
  return (
    <Modal open={open} onClose={onClose} label="About this archive">
      <div className="p-6 pt-12">
        <div className="mono text-xs uppercase tracking-[0.2em] text-brand-primary">About this archive</div>
        <h3 className="mt-2 text-2xl font-extrabold">A car, reconstructed from paper</h3>
        <div className="mt-4 space-y-3 text-sm leading-relaxed text-ink/90">
          <p>
            A 1965 Volkswagen Karmann Ghia was restored between 2013 and 2018, bought as a 500 dollar project car.
            Its prior restorer kept a folder: counter receipts on thermal paper, multi page mail order invoices, a
            packing list, product literature, and one page of lined notebook paper that turned out to be the most
            valuable document in the box.
          </p>
          <p>
            Every page was photographed, read, and normalized into a single structured record across eleven extraction
            batches. Parts and services, vendors, documents, build specifications, a timeline, and the open questions
            are all derived from that one file. Inferences are flagged, corrections are kept beside the claims they
            corrected, and uncertainty is recorded rather than smoothed over.
          </p>
          <p>
            This site is the readable face of that record. It adds no facts of its own. The numbers you see are summed
            from the data at load time.
          </p>
        </div>
        <dl className="mono mt-5 grid grid-cols-2 gap-x-6 gap-y-1 border-t border-line pt-4 text-xs text-ink-muted">
          <div className="flex justify-between"><dt>Record version</dt><dd className="text-ink">{a.raw.schema_version}</dd></div>
          <div className="flex justify-between"><dt>Documents</dt><dd className="text-ink">{a.totals.documents}</dd></div>
          <div className="flex justify-between"><dt>Provenance</dt><dd className="text-ink">{a.raw.generated_from}</dd></div>
          <div className="flex justify-between"><dt>Generated</dt><dd className="text-ink">{a.raw.generated_date}</dd></div>
        </dl>
      </div>
    </Modal>
  )
}
