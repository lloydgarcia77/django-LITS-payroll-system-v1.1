$( function() {     
    const value = JSON.parse(document.getElementById("list_of_users_data_render").textContent);
    const arrUser = value.list_of_users;    
    for(var x=0; x<arrUser.length; x++){ 
        $(`<div>${arrUser[x]}</div>`).data("name",arrUser[x]).attr('id',x).appendTo('#user_piles').draggable({
            containment: '#content',
            stack: '#user_piles div',
            cursor: 'move',
            revert : function(event, ui) {
                // on older version of jQuery use "draggable"
                // $(this).data("draggable")
                $(this).data("draggable").originalPosition = {
                    top : 0,
                    left : 0
                };
                return !event;
                // return (event !== false) ? false : true;
            }
        });   
    }

    $( "#user_piles, #col_manager" ).sortable({
        connectWith: ".col_roles"
    }).disableSelection();
  
    
 
    $("#addMD").click(function(e){ 
        $(`<div>M. Director</div>`).appendTo("#col_manager").droppable({
            // accept: '#name',
             hoverClass: 'hovered', 
             drop: function( event, ui ) {   
                 //$(this).droppable( 'disable' );
                 ui.draggable.position( { of: $(this), my: 'left top', at: 'left top' } ); 
                 // ui.draggable.draggable('option', 'revert', true);
             }
         });  ;
    });
    $("#addHR").click(function(e){ 
        $(`<div>Human Resource</div>`).appendTo("#col_hr").droppable({
            // accept: '#name',
             hoverClass: 'hovered', 
             drop: function( event, ui ) {   
                 //$(this).droppable( 'disable' );
                 ui.draggable.position( { of: $(this), my: 'left top', at: 'left top' } ); 
                 // ui.draggable.draggable('option', 'revert', true);
             }
         });  ;;
    });
    $("#addBUH").click(function(e){ 
        $(`<div>B.U Head</div>`).appendTo("#col_buh").droppable({
            // accept: '#name',
             hoverClass: 'hovered', 
             drop: function( event, ui ) {   
                 //$(this).droppable( 'disable' );
                 ui.draggable.position( { of: $(this), my: 'left top', at: 'left top' } ); 
                 // ui.draggable.draggable('option', 'revert', true);
             }
         });  ;;
    });
    

  } ); 