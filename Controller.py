import Text as tf
import View
import Model


def start():
    while True:
        choice = View.main_menu()
        match choice:
            case 1:
                Model.open_file()
                View.print_message(tf.open_successful)
            case 2:
                Model.save_file()
                View.print_message(tf.save_successаul)
            case 3:
                pb = Model.notes
                View.show_note(pb, tf.no_phone_book)
            case 4:
                new_contact = View.input_note(tf.new_note)
                Model.add_contact(new_contact)
                View.print_message(tf.add_successful)
            case 5:
                contact = View.find_data()
                pb = Model.notes
                View.show_note(Model.find_date(contact, pb), tf.no_phone_book)
            case 6:
                contact = View.find_name()
                pb = Model.notes
                View.show_note(Model.find_name(contact, pb), tf.no_phone_book)
            case 7:
                pb = Model.notes
                View.show_note(pb, '')
                choice = View.input_choice(len(pb), tf.change_choice) - 1
                change_contact = View.input_note(tf.change_note)
                res = Model.change(choice, change_contact)
                View.print_message(tf.changed(res['name']))
            case 8:
                pb = Model.get_pb()
                name = Model.del_contact(View.input_index(tf.index_del_contact, pb, tf.load_error))
                View.print_message(tf.del_contact(name))
            case 9:
                View.print_message(View.close())
                break