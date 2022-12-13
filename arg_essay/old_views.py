# def thesis_support(request):
#     form = Supports
#     bobblypop = Thesis.objects.filter(user=request.user)
#     if request.method == 'POST':
#         try:
#             form = SupportsForm(request.POST)
#             if form.is_valid():
#                 form.instance.user = request.user
#                 form.save()
#                 return redirect('thesis-statement')
#         except:
#             None
#     context = {'form': form, 'bobblypop': bobblypop}
#     return render(request, 'essay_supports.html', context)


# def thesis_statement(request):
#     supps = Supports.objects.filter(user=request.user)
#     statement = Thesis.objects.filter(user=request.user)
#     context = {'statement': statement, 'supps': supps}
#     return render(request, 'thesis_statement.html', context)