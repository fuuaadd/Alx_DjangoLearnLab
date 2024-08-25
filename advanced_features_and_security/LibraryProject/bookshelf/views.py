from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Document

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        document.title = request.POST.get('title')
        document.content = request.POST.get('content')
        document.save()
        return redirect('document_detail', document_id=document.id)
    return render(request, 'relationship_app/edit_document.html', {'document': document})
