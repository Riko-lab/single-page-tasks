def show_tasks(tasks):
    template = '<ul class="tasks">\
                    <li>\
                        <span>ID</span>\
                        <h3>TITLE</h3>\
                    </li>'
    for task in tasks:
        template += f'<li class="task-id" data-id="{task[0]}">\
                        <span>{task[0]}</span>\
                        <h4 class="task-title">{task[1]}</h4>\
                      </li>'
    template += '</ul>'
    return template

def show_single_task(task_id, task_title, task_note):
    template = f'<div class="single-task-cnt">\
                    <button id="close" class="black-btn"><i class="fas fa-times"></i></button>\
                    <div class="single-task-id">\
                        <span>ID task: {task_id}</span>\
                    </div>\
                    <div class="single-body">\
                        <h3>{task_title}</h3>\
                        <p>{task_note}</p>\
                    </div>\
                </div>'
    return template
    
